class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # user, task, priority

        self.heap = []
        self.priority = {}
        self.task_to_user = {}
        for userId, taskId, priority in tasks:
            heapq.heappush(self.heap, (-priority, -taskId, userId))
            self.priority[taskId] = priority
            self.task_to_user[taskId] = userId

    def add(self, userId: int, taskId: int, priority: int) -> None:

        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.task_to_user[taskId] = userId
        self.priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_to_user[taskId]
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))
        self.priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.priority[taskId] = None

    def execTop(self) -> int:

        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            priority, taskId = -priority, -taskId
            # corner case: A task can be removed and then added back as different user with same priority,
            # So we also need to check if user are same
            if priority != self.priority[taskId] or userId != self.task_to_user[taskId]:
                # stale heap entry, lazy delete
                continue
            else:
                # valid heap entry
                self.priority[taskId] = None
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()