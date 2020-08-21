# Serverless Data API with Azure Functions
A short example that demonstrates how to use Azure Functions and Azure Blob Storage to build a serverless data sharing API. The sample uses a HTTP Trigger and Blob storage input binding, to return data from a file over HTTP.

## Instructions for use
1. Ensure you have the pre-requisite tools and extensions for Azure Functions development (VS Code, the Azure Functions Extension, and Azure Functions Core Tools are recommended - you can find [more details on getting started here](https://github.com/joe-plumb/functions-demo))
1. Clone this repo to your local machine using `git clone ..`
1. `cd` into the folder, and launch VS code with `code .`
1. Create a `local.settings.json` file with the following structure. Update the `MyStorageConnectionAppSetting` with the connection string to your storage account that you would like to share data from.
```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "MyStorageConnectionAppSetting": "$STORAGE_CONNECTION_STRING"
  }
}
```
1. In your storage account, create a storage container called `data`, add a folder, and a file within that folder, e.g. `/curated/data.txt`. If you want to point the function at an existing container, you can update this in the `path` value of the `inputblob` binding in the `function.json` file.

### Local emulation
1. Run the function locally by running `func start`, or starting debug mode in VS Code (Run > Start Debugging, or press F5)
1. Retrieve data by heading to the url in your browser, or issuing a curl request against the endpoint, e.g. 
```
curl http://localhost:7071/api/data/curated/data.txt
```

### Running in Azure Functions on Azure
Details on how to package and deploy your function can be found [in the documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#publishing-to-azure)

## Limitations
- *NB:* This example function does not include any authentication mechanism - deploying as-is, with a connection your storage account is not advised (unless of course this is what you are attempting to achieve!) as it is creating a publically callable endpoint into your storage account. If the data in your storage account is sensitive in nature, *do not do this*.
- This function returns a `404` error if the folder or file does not exist. It would be great to instead return a list of available files within the folder for download.
