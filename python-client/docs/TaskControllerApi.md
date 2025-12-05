# openapi_client.TaskControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TaskControllerApi.md#create_task) | **POST** /api/tasks | 
[**delete_task**](TaskControllerApi.md#delete_task) | **DELETE** /api/tasks/{id} | 
[**disable_task_reminder**](TaskControllerApi.md#disable_task_reminder) | **PUT** /api/tasks/{id}/disable-reminder | 
[**enable_task_reminder**](TaskControllerApi.md#enable_task_reminder) | **PUT** /api/tasks/{id}/enable-reminder | 
[**get_all_tasks**](TaskControllerApi.md#get_all_tasks) | **GET** /api/tasks | 
[**get_task_by_id**](TaskControllerApi.md#get_task_by_id) | **GET** /api/tasks/{id} | 
[**get_task_statistics**](TaskControllerApi.md#get_task_statistics) | **GET** /api/tasks/statistics | 
[**get_tasks_by_completed**](TaskControllerApi.md#get_tasks_by_completed) | **GET** /api/tasks/completed/{isCompleted} | 
[**get_tasks_by_date_range**](TaskControllerApi.md#get_tasks_by_date_range) | **GET** /api/tasks/date-range | 
[**get_tasks_by_location**](TaskControllerApi.md#get_tasks_by_location) | **GET** /api/tasks/location | 
[**mark_task_as_completed**](TaskControllerApi.md#mark_task_as_completed) | **PUT** /api/tasks/{id}/complete | 
[**mark_task_as_uncompleted**](TaskControllerApi.md#mark_task_as_uncompleted) | **PUT** /api/tasks/{id}/uncomplete | 
[**search_tasks_by_title**](TaskControllerApi.md#search_tasks_by_title) | **GET** /api/tasks/search | 
[**toggle_task_completion**](TaskControllerApi.md#toggle_task_completion) | **PUT** /api/tasks/{id}/toggle | 
[**update_task**](TaskControllerApi.md#update_task) | **PUT** /api/tasks/{id} | 


# **create_task**
> Task create_task(task)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

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

    try:
        api_response = api_instance.create_task(task)
        print("The response of TaskControllerApi->create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> bool delete_task(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.delete_task(id)
        print("The response of TaskControllerApi->delete_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_task_reminder**
> bool disable_task_reminder(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.disable_task_reminder(id)
        print("The response of TaskControllerApi->disable_task_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->disable_task_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_task_reminder**
> bool enable_task_reminder(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.enable_task_reminder(id)
        print("The response of TaskControllerApi->enable_task_reminder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->enable_task_reminder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tasks**
> List[Task] get_all_tasks()

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)

    try:
        api_response = api_instance.get_all_tasks()
        print("The response of TaskControllerApi->get_all_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_all_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_by_id**
> Task get_task_by_id(id)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_task_by_id(id)
        print("The response of TaskControllerApi->get_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_statistics**
> Dict[str, int] get_task_statistics()

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)

    try:
        api_response = api_instance.get_task_statistics()
        print("The response of TaskControllerApi->get_task_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_task_statistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_by_completed**
> List[Task] get_tasks_by_completed(is_completed)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    is_completed = True # bool | 

    try:
        api_response = api_instance.get_tasks_by_completed(is_completed)
        print("The response of TaskControllerApi->get_tasks_by_completed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_tasks_by_completed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_completed** | **bool**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_by_date_range**
> List[Task] get_tasks_by_date_range(start_date, end_date)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    start_date = 56 # int | 
    end_date = 56 # int | 

    try:
        api_response = api_instance.get_tasks_by_date_range(start_date, end_date)
        print("The response of TaskControllerApi->get_tasks_by_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_tasks_by_date_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**|  | 
 **end_date** | **int**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_by_location**
> List[Task] get_tasks_by_location(latitude, longitude, radius)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    latitude = 3.4 # float | 
    longitude = 3.4 # float | 
    radius = 3.4 # float | 

    try:
        api_response = api_instance.get_tasks_by_location(latitude, longitude, radius)
        print("The response of TaskControllerApi->get_tasks_by_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->get_tasks_by_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**|  | 
 **longitude** | **float**|  | 
 **radius** | **float**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_task_as_completed**
> bool mark_task_as_completed(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.mark_task_as_completed(id)
        print("The response of TaskControllerApi->mark_task_as_completed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->mark_task_as_completed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_task_as_uncompleted**
> bool mark_task_as_uncompleted(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.mark_task_as_uncompleted(id)
        print("The response of TaskControllerApi->mark_task_as_uncompleted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->mark_task_as_uncompleted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks_by_title**
> List[Task] search_tasks_by_title(title)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    title = 'title_example' # str | 

    try:
        api_response = api_instance.search_tasks_by_title(title)
        print("The response of TaskControllerApi->search_tasks_by_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->search_tasks_by_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_task_completion**
> bool toggle_task_completion(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.toggle_task_completion(id)
        print("The response of TaskControllerApi->toggle_task_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->toggle_task_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(id, task)

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TaskControllerApi(api_client)
    id = 56 # int | 
    task = openapi_client.Task() # Task | 

    try:
        api_response = api_instance.update_task(id, task)
        print("The response of TaskControllerApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskControllerApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **task** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

