# GeoTask MCP Server

一个基于 Model Context Protocol (MCP) 的地理任务管理服务器，提供地理位置相关的任务管理功能。

## 项目概述

GeoTask MCP Server 是一个功能强大的任务管理系统，特别针对地理位置相关的任务进行了优化。通过 MCP 协议，它可以与各种 AI 助手和客户端无缝集成，提供智能的任务管理服务。

## 主要功能

### 🗺️ 地理位置功能
- **位置感知任务**：支持为任务添加具体的地理位置信息
- **地理围栏**：设置地理围栏半径，实现基于位置的任务提醒
- **位置搜索**：根据经纬度和半径搜索附近任务

### 📋 任务管理
- **创建任务**：创建包含标题、描述、截止日期等信息的任务
- **任务状态管理**：标记任务完成/未完成状态
- **任务搜索**：按标题搜索任务
- **任务统计**：获取任务完成情况统计信息
- **日期范围查询**：按日期范围筛选任务

### 🔔 提醒功能
- **启用/禁用提醒**：为单个任务控制提醒功能
- **智能提醒**：基于时间和位置的智能提醒系统

## 技术架构

### 核心技术栈
- **FastMCP**: 基于 Python 的 MCP 服务器框架
- **OpenAPI Client**: 自动生成的 API 客户端
- **Pydantic**: 数据验证和序列化

### 支持的传输协议
- **Streamable HTTP**: 支持流式 HTTP 传输

## 安装和配置

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/MoQiii/MCP_Server.git
cd MCP_Server
```

2. **创建虚拟环境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

### 配置说明

服务器默认配置：
- **MCP 服务器地址**: `localhost:8081`
- **后端 API 地址**: `http://localhost:8080`

如需修改配置，请编辑 `simple_mcp_server.py` 文件中的相应参数。

## 使用方法

### 启动服务器

```bash
python simple_mcp_server.py
```

服务器启动后，将在指定端口监听 MCP 请求。

### 可用工具

#### 1. add_numbers
计算数字列表的和。

**参数：**
- `numbers`: 数字列表 (List[float])

**示例：**
```python
# 计算数字和
result = add_numbers([1, 2, 3, 4, 5])
# 返回: 15
```

#### 2. 添加任务
向系统中添加新任务。

**参数：**
- `task`: Task 对象，包含以下字段：
  - `title`: 任务标题
  - `description`: 任务描述
  - `dueDate`: 截止日期 (时间戳)
  - `dueTime`: 截止时间 (时间戳)
  - `isCompleted`: 是否完成
  - `isReminderEnabled`: 是否启用提醒
  - `location`: 位置描述
  - `latitude`: 纬度
  - `longitude`: 经度
  - `geofenceRadius`: 地理围栏半径

**示例：**
```python
from openapi_client.models.task import Task

# 创建任务
task = Task(
    title="购买咖啡",
    description="去星巴克购买拿铁咖啡",
    location="星巴克",
    latitude=31.2304,
    longitude=121.4737,
    geofenceRadius=100.0
)

# 添加任务
add_task(task)
```

## API 接口（基于geo_task_server）

后端提供完整的 RESTful API，支持以下操作：

### 任务管理
- `POST /api/tasks` - 创建任务
- `GET /api/tasks` - 获取所有任务
- `GET /api/tasks/{id}` - 获取指定任务
- `PUT /api/tasks/{id}` - 更新任务
- `DELETE /api/tasks/{id}` - 删除任务

### 任务状态
- `PUT /api/tasks/{id}/complete` - 标记任务完成
- `PUT /api/tasks/{id}/uncomplete` - 标记任务未完成
- `PUT /api/tasks/{id}/toggle` - 切换任务状态

### 提醒管理
- `PUT /api/tasks/{id}/enable-reminder` - 启用提醒
- `PUT /api/tasks/{id}/disable-reminder` - 禁用提醒

### 查询功能
- `GET /api/tasks/search` - 按标题搜索
- `GET /api/tasks/completed/{isCompleted}` - 按完成状态查询
- `GET /api/tasks/date-range` - 按日期范围查询
- `GET /api/tasks/location` - 按位置查询
- `GET /api/tasks/statistics` - 获取统计信息

## 客户端 SDK

项目提供了多种语言的客户端 SDK：

### Python 客户端
位于 `python-client/` 目录，包含：
- 完整的 API 客户端
- 数据模型定义
- 使用示例和文档

### 使用 Python 客户端

```python
import openapi_client
from openapi_client.models.task import Task

# 配置客户端
configuration = openapi_client.Configuration(
    host="http://localhost:8080"
)

# 使用客户端
with openapi_client.ApiClient(configuration) as api_client:
    api_instance = openapi_client.TaskControllerApi(api_client)
    
    # 获取所有任务
    tasks = api_instance.get_all_tasks()
    print(tasks)
```

## 开发和测试

### 运行测试
```bash
# 运行 Python 客户端测试
python test/openapi_client_test.py
```

### 项目结构
```
GeoTask_MCP_Server/
├── simple_mcp_server.py          # MCP 服务器主文件
├── requirements.txt               # Python 依赖
├── README.md                      # 项目文档
├── python-client/                 # Python 客户端 SDK
│   ├── openapi_client/           # 生成的 API 客户端
│   ├── docs/                     # API 文档
│   └── test/                     # 测试文件
└── test/                         # 服务器测试文件
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目主页: https://github.com/MoQiii/MCP_Server
- 问题反馈: https://github.com/MoQiii/MCP_Server/issues

## 更新日志

### v1.0.0
- 初始版本发布
- 支持基本的任务管理功能
- 集成地理位置功能
- 提供 MCP 协议支持
