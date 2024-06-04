import os
import logging
import azure
import azure.functions as func

from azure.core.exceptions import ClientAuthenticationError, ResourceNotFoundError
from azure.data.tables import TableServiceClient, TableClient
from azure.core.credentials import AzureNamedKeyCredential
from dotenv import load_dotenv

load_dotenv()
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
# app.add_storage()

# Load connection string from environment variable (assuming a .env file)
# conn_str = os.environ['the_connection_string']
# table_name = os.environ['table_name']
conn_str = os.getenv('the_connection_string')
table_name = os.getenv('table_name')




logging.info(conn_str)
# Create a TableClient object using the connection string
table_service_client = TableServiceClient.from_connection_string(conn_str=conn_str)
table_client = table_service_client.get_table_client(table_name=table_name)

# creating the structure of entity from table
visitor_entry = {
    'PartitionKey' : "VisitorsCount",
    'RowKey' : "resume_visitors",
    'value' : 0
}


# @azure.functions.function.FunctionName("visitorCount")
@app.function_name(name="visitorCount")
@app.route(route="count/{new_visitor?}", auth_level=func.AuthLevel.ANONYMOUS)
def main(req : func.HttpRequest) -> func.HttpResponse:
    
    # checking to see if there is a new visitor based on url parameters
    new_visitor = True if req.route_params.get('new_visitor') else False

    logging.info(f"\n\n{'NEW VISITOR' if new_visitor else 'NO NEW VISITOR'}\n\n")
    
    # error handling
    if not conn_str:
        return func.HttpResponse(
        body='Error: Missing COSMOSDB_CONNECTION_STRING environment variable.',
        status_code=500
        )

    logging.info("HTTP trigger function processed a request. ")
    try:
        count = table_client.get_entity(partition_key="VisitorsCount",row_key="resume_visitors")
        if count:
            """Updates the 'visitors_count' value in the 'visitors' entry."""
            if new_visitor:
                count['value'] += 1
                try:
                    table_client.update_entity(entity=count)
                    logging.info(f"Visitor count updated to: {count['value']}")
                
                except LookupError as e:
                    logging.error(f"Entity not found: {e}")
                    return func.HttpResponse (
                        status_code= 500,
                        body=f"{e}"
                    )
                except ClientAuthenticationError as e:
                    logging.error(f"Connection error: {e}")
                    return func.HttpResponse (
                        status_code= 500,
                        body=f"{e}"
                    )
                except Exception as e:
                    logging.error(f"Unexpected error: {e}")
                    return func.HttpResponse (
                        status_code= 500,
                        body=f"{e}"
                    )
            else:
                    return func.HttpResponse (
                    status_code= 200,
                    body=f"Visitor count is {count['value']}."
                )
    except ResourceNotFoundError:
        """Creates an entry with key 'visitors' and value 0 in the Cosmos DB table."""
        logging.info("Resource not found. Creating resource")
        try:
            table_client.create_entity(entity=visitor_entry)
            logging.info("Visitor entry created successfully!")
            return func.HttpResponse (
            status_code= 200,
            body="Visitor count created."
            )
        except Exception as e:
            logging.info(f"Error creating entry: {e}")
            return func.HttpResponse (
                status_code= 500,
                body=f"Error creating visitor count entry {e}."
            )


    return func.HttpResponse (
        status_code= 200,
        body=f"Visitor count incremented to {count['value']}."
    )