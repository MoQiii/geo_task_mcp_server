from dataclasses import dataclass, field
from typing import Optional
import time


@dataclass
class Task:
    """
    任务数据类，对应Kotlin中的Task data class
    """
    id: int = 0  # 主键，自动生成
    title: str = ""  # 任务标题
    description: str = ""  # 任务描述
    due_date: int = 0  # 截止日期时间戳
    due_time: int = 0  # 截止时间时间戳
    is_completed: bool = False  # 是否已完成
    is_reminder_enabled: bool = False  # 是否启用提醒
    location: Optional[str] = None  # 地址描述
    latitude: Optional[float] = None  # 纬度
    longitude: Optional[float] = None  # 经度
    geofence_radius: float = 200.0  # 地理围栏半径（米）
    created_at: int = field(default_factory=lambda: int(time.time() * 1000))  # 创建时间戳（毫秒）
    updated_at: int = field(default_factory=lambda: int(time.time() * 1000))  # 更新时间戳（毫秒）

    # def __post_init__(self):
    #     """
    #     初始化后的处理，确保时间戳为毫秒级别
    #     """
    #     if self.created_at == 0:
    #         self.created_at = int(time.time() * 1000)
    #     if self.updated_at == 0:
    #         self.updated_at = int(time.time() * 1000)

    # def mark_completed(self):
    #     """
    #     标记任务为已完成
    #     """
    #     self.is_completed = True
    #     self.updated_at = int(time.time() * 1000)

    # def mark_incomplete(self):
    #     """
    #     标记任务为未完成
    #     """
    #     self.is_completed = False
    #     self.updated_at = int(time.time() * 1000)

    # def enable_reminder(self):
    #     """
    #     启用提醒
    #     """
    #     self.is_reminder_enabled = True
    #     self.updated_at = int(time.time() * 1000)

    # def disable_reminder(self):
    #     """
    #     禁用提醒
    #     """
    #     self.is_reminder_enabled = False
    #     self.updated_at = int(time.time() * 1000)

    # def set_location(self, location: str, latitude: float, longitude: float, radius: float = 200.0):
    #     """
    #     设置位置信息
    #     """
    #     self.location = location
    #     self.latitude = latitude
    #     self.longitude = longitude
    #     self.geofence_radius = radius
    #     self.updated_at = int(time.time() * 1000)

    # def clear_location(self):
    #     """
    #     清除位置信息
    #     """
    #     self.location = None
    #     self.latitude = None
    #     self.longitude = None
    #     self.updated_at = int(time.time() * 1000)

    # def to_dict(self) -> dict:
    #     """
    #     转换为字典格式
    #     """
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'description': self.description,
    #         'due_date': self.due_date,
    #         'due_time': self.due_time,
    #         'is_completed': self.is_completed,
    #         'is_reminder_enabled': self.is_reminder_enabled,
    #         'location': self.location,
    #         'latitude': self.latitude,
    #         'longitude': self.longitude,
    #         'geofence_radius': self.geofence_radius,
    #         'created_at': self.created_at,
    #         'updated_at': self.updated_at
    #     }

    # @classmethod
    # def from_dict(cls, data: dict) -> 'Task':
    #     """
    #     从字典创建Task实例
    #     """
    #     return cls(
    #         id=data.get('id', 0),
    #         title=data.get('title', ''),
    #         description=data.get('description', ''),
    #         due_date=data.get('due_date', 0),
    #         due_time=data.get('due_time', 0),
    #         is_completed=data.get('is_completed', False),
    #         is_reminder_enabled=data.get('is_reminder_enabled', False),
    #         location=data.get('location'),
    #         latitude=data.get('latitude'),
    #         longitude=data.get('longitude'),
    #         geofence_radius=data.get('geofence_radius', 200.0),
    #         created_at=data.get('created_at', int(time.time() * 1000)),
    #         updated_at=data.get('updated_at', int(time.time() * 1000))
    #     )
