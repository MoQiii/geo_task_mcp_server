import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

def test():
    # Defining the host is optional and defaults to http://localhost:8080
    # See configuration.py for a list of all supported configuration parameters.
    configuration = openapi_client.Configuration(
        host = "http://localhost:8080"
    )


    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.TaskControllerApi(api_client)
        task = openapi_client.Task() # Task | 
        # task对象设置属性
        task.title = "Sample Task"
        task.description = "This is a sample task created via OpenAPI client."
        task.due_date = 1700000000000
        task.due_time = 1700003600000
        task.is_completed = False
        task.is_reminder_enabled = True
        task.location = "123 Sample St, Sample City"
        task.latitude = 37.7749
        task.longitude = -122.4194
        task.geofence_radius = 150.0
        try:
            api_response = api_instance.create_task(task)
            print("The response of TaskControllerApi->create_task:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling TaskControllerApi->create_task: %s\n" % e)


# 运行服务器
if __name__ == "__main__":
    test()