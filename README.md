# Hafsa's Portfolio

## Portfolio Website with Azure Functions and Cosmos DB

This project demonstrates a portfolio website that leverages Azure Functions and Cosmos DB to track visitor count. The website is built with HTML and deployed as a static website on Azure Blob Storage.

### Technologies Used

* Azure Functions (Python)
* Cosmos DB
* Azure Blob Storage
* HTML

### Project Structure

```
README.md
backend/
  visitor-count-function/
    visitor-count-function/
        function_app.py
        host.json
        requirements.txt
frontend/
  index.html
  css/
  fonts/
  images/
  js/

  ... (other HTML files and assets)
.env 
```

### Deployment Steps

1. **Azure Cosmos DB Table**

2. **Develop Azure Function**
    * Used an `.env` file during local development but cofigured environmentals variable for production.
    * The Azure Function code resides in the `backend/visitor-count-function` directory.
    * The `function.py` file defines a function that:
        * Connects to Cosmos DB table using the connection string from the environment variable.
        * Checks if a visitor entry exists.
        * If a visitor entry exists, increments the visitor count.
        * If no visitor entry exists, creates a new entry with a count of 1.
        * Returns a response indicating the updated visitor count.

3. **Develop Static Website**
    * The static website files (HTML, CSS, JavaScript) are located in the `frontend` directory.
    * The website includes a mechanism to call the Azure Function and display the visitor count.
    * Used a template to make the website.
    * Authenticates against unique visitors using cookies.

4. **CI/CD**
    * Implemented CI/CD pipeline using GitHub Actions to automate the deployment process for  function app and static website.

### Resources and Links Used

* [https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables#getting-started](Azure Functions DSK)
* [https://learn.microsoft.com/en-us/azure/cosmos-db/](Cosmos DB documentation)
* Azure Blob Storage documentation: [https://learn.microsoft.com/en-us/azure/storage/blobs/](https://learn.microsoft.com/en-us/azure/storage/blobs/)
* https://stackoverflow.com/questions/69058910/limit-azure-functions-call-from-static-website-in-blob-storage
* [https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-static-site-github-actions?tabs=userlevel](CI/CD for static website deployment)
* [GitHub Worflow Samples](https://github.com/Azure/actions-workflow-samples)

