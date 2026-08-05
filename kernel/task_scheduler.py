from collections import deque


class TaskScheduler:
    """
    FIFO Task Scheduler.
    """

    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        """
        Add a task.
        """

        self.queue.append(task)

        print(f"[Scheduler] Added: {task.name}")

    def get_next_task(self):
        """
        Get the next task.
        """

        if not self.queue:
            return None

        return self.queue.popleft()

    def has_tasks(self):
        """
        Returns True if tasks exist.
        """

        return len(self.queue) > 0

    def queue_size(self):
        """
        Number of queued tasks.
        """

        return len(self.queue)