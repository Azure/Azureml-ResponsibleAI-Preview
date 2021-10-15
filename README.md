# Azure Machine Learning Responsible AI Dashboard - Private Preview

## What is this new feature?

## Supported scenarios, models and datasets

## Set Up
In this section, we will go over the basic setup steps that you need in order to generate responsible AI insights for your models from SDK and visualize the generated responsible AI insights in [AML studio](https://ml.azure.com/).

### Installing `azureml-responsibleai` SDK
In order to install `azureml-responsibleai` package you will need a python virtual environment. You can create a python virtual environment using `conda`.
```c
conda create -n azureml_env python=3.6.12 nb_conda -y
```

Once the `conda` environment `azureml_env` is created, you can install `azureml-responsibleai` using `pip`.

```c
activate azureml_env
pip install azureml-responsibleai
pip install liac-arff
```

### Create an Azure subscription
Create an Azure workspace by using the [configuration notebook](https://github.com/Azure/MachineLearningNotebooks/blob/master/configuration.ipynb)

### Generating responsibleai AI insights
Once you have installed `azureml-responsibleai` and created an Azure workspace, you can execute the responsibleai notebooks in the `notebooks` folder in this repo.

### Viewing your Responsible AI Dashboard in the AzureML studio portal

## Responsible AI Dashboard walkthrough and sample notebooks

## What Next?: How to join Private Preview
We are super excited for you to try this new feature in AzureML! 
- Reach out to - mithigpe@microsoft.com to enable your Azure subscription for this Private Preview feature.
- In addition, fill out this form - Private Preview sign up for [Responsible AI Dashboard in AzureML](https://forms.office.com/r/R6PmBCkyWb)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
