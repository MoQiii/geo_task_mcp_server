from fastmcp import FastMCP
from typing import List
from openapi_client.models.task import Task
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# 创建 MCP 路由器
mcp = FastMCP(host="10.16.36.125", port=8081)
configuration=None

# 定义加法工具
@mcp.tool()
def add_numbers(numbers: List[float]) -> float:
    """
    返回数字列表的和。
    
    :param numbers: 数字列表
    :return: 数字列表的和
    """
    return sum(numbers)

@mcp.tool(
    name="添加任务", 
    description="添加任务到任务到系统",
    
)
# def add_task(task:Task):
#     # Enter a context with an instance of the API client
#     with openapi_client.ApiClient(configuration) as api_client:
#         # Create an instance of the API class
#         api_instance = openapi_client.TaskControllerApi(api_client)
#         try:
#             api_response = api_instance.create_task(task)
#             print("The response of TaskControllerApi->create_task:\n")
#             pprint(api_response)
#         except Exception as e:
#             print("Exception when calling TaskControllerApi->create_task: %s\n" % e)

def add_task(
    title: str = None,
    description: str = None,
    due_date: int = None,
    due_time: int = None,
    is_completed: bool = None,
    is_reminder_enabled: bool = None,
    location: str = None,
    latitude: float = None,
    longitude: float = None,
    geofence_radius: float = None,
    created_at: int = None,
    updated_at: int = None
):
    # 组装 Task 对象
    task = Task(
        title=title,
        description=description,
        dueDate=due_date,
        dueTime=due_time,
        isCompleted=is_completed,
        isReminderEnabled=is_reminder_enabled,
        location=location,
        latitude=latitude,
        longitude=longitude,
        geofenceRadius=geofence_radius,
        createdAt=created_at,
        updatedAt=updated_at
    )

    # 调用 API
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.TaskControllerApi(api_client)
        try:
            api_response = api_instance.create_task(task)
            print("The response of TaskControllerApi->create_task:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling TaskControllerApi->create_task: %s\n" % e)


# 运行服务器
if __name__ == "__main__":
    configuration = openapi_client.Configuration(
        host = "http://localhost:8080"
    )
    mcp.run(transport="streamable-http")
