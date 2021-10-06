# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Sample train script for azureml-responisbleai notebooks."""

import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from azureml.core.dataset import Dataset
from azureml.core.run import Run


def get_classification_model_pipeline(continuous_features,
                                      categorical_features):
    # We create the preprocessing pipelines for both numeric
    # and categorical data.
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer()),
        ('scaler', StandardScaler())])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    transformations = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, continuous_features),
            ('cat', categorical_transformer, categorical_features)])

    # Append classifier to preprocessing pipeline.
    # Now we have a full prediction pipeline.
    pipeline = Pipeline(steps=[('preprocessor', transformations),
                               ('classifier', RandomForestClassifier())])

    return pipeline


# Get workspace from the run context
run = Run.get_context()
ws = run.experiment.workspace
run.display_name = 'adult_train'

# Get the train dataset from the workspace
train_dataset = Dataset.get_by_name(workspace=ws, name='adult_train')

# Drop the labeled column to get the training set.
X_train = train_dataset.drop_columns(
    columns=["income"]).to_pandas_dataframe()
y_train = train_dataset.keep_columns(
    columns=["income"], validate=True).to_pandas_dataframe().values

continuous_features = ['age', 'hours-per-week', 'fnlwgt', 'education-num',
                       'capital-gain', 'capital-loss']
categorical_features = X_train.columns.difference(continuous_features).tolist()

pipeline = get_classification_model_pipeline(
    continuous_features=continuous_features,
    categorical_features=categorical_features)
model = pipeline.fit(X_train, y_train)

# Register the trained model
model_path = 'adult.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
run.upload_file('adult.pkl', 'adult.pkl')

registered_model = run.register_model(model_path='adult.pkl',
                                      model_name='adult')
