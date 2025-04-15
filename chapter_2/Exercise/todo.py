import datetime as dt


class Task:
    _id: str = 1

    def __init__(self, name: str):
        self.name: str = name
        self.__creation_date: str = dt.date.today()
        self.__creation_time: str = dt.datetime.now().time().strftime("%H:%M")
        self.done = False
        self.id = Task._id
        Task._id += 1

    def match_task(self, filter):
        return filter in self.name

    def check_task(self):
        return self.done


class Todo:
    def __init__(self):
        self.tasks: list[Task] = []
        
    def _find_task(self, id: int):
        for task in self.tasks:
            if id == task.id:
                return task
        return None 
    
    def _check_tasks(self):
        return False if not self.tasks else True

    def add_task(self, name: str):
        self.tasks.append(Task(name))
        print("Task has been added.")

    def modify_task(self, id: int, new_name: str) -> bool:
        if self._check_tasks():
            print("There no task added yet!")
        task = self._find_task(id)
        if task:
            task.name = new_name
            return True
        return False
            

    def delete_task(self, id: int) -> bool:
        if self._check_tasks():
            print("There nothing to delete nothing has been added yet!")

        task = self._find_task(id)
        if task:
            self.tasks.remove(task)
            return True
        else:
            return False

    def mark_task(self, id: int, done: bool = True):
        if self._check_tasks():
            print("There no task to mark it")

        task = self._find_task(id)
        if task:
            task.done = done
            return True
        else:
            print("Dont have this task")
            return False
