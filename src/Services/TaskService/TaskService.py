from collections import deque

from src.Services.BaseService import BaseService
from typing import Callable

from src.Services.Exeptions import ArgumentError


class TaskService(BaseService, deque):

    def __init__(self, default_handler=None, *args, **kwargs):
        self.default_handler = default_handler
        super(TaskService, self).__init__(*args, **kwargs)

    def has_tasks(self):
        return self  # Empty deque is falsy

    def get_task(self):
        return self.popleft()

    def add_task(self, task_data: dict, handler: Callable = None):
        """Add task to queue."""

        if not isinstance(task_data, dict):
            raise ArgumentError("Expected a dictionary as task_data.")
        if not callable(handler) and not self.default_handler:
            raise ArgumentError("Expected a callable as handler.")
        handler = handler or self.default_handler
        self.append((handler, task_data))
