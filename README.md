# Prompt flow Sample

This repository demonstrates how to develop a Prompt flow flow in a local environment.

## About the Prompt flow Python library
Prompt flow Python library has been created by Microsoft.
It allows the local development of flows use pure python or low-code approaches with the help of the Prompt flow extension for VS Code.

- [Prompt flow Documentation](https://microsoft.github.io/promptflow/index.html)
- [Prompt flow VS Code Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

> [!NOTE]  
> This repository use pure python and Azure OpenAI to demostrate how to build a simple chat flow.

## Execute the code
1. Create a python environment
```
python -m venv venv
```

2. Install the `requirements.txt` file
```
python -r requirements.txt
```

3. Create the following `.env` file in the root of the project
```
# AOAI
AOAI_ENDPOINT     = <Azure OpenAI Endpoint>
AOAI_API_KEY      = <Azure OpenAI API Key>
AOAI_API_VERSION  = <OpenAI API Version>
AOAI_DEPLOYMENT   = <Name of the deployment of the model in Azure OpenAI>
```
4. Execute the code
```
python flow_chat.py
```

## TO DO
- [ ] Add support for OpenAI API
- [ ] Explain in detail the code
- [ ] Implement the low-code (visual flow)
