from todo import Todo, Task

from sys import exit


class Menu:
    def __init__(self):
        self.todo = Todo()
        self.choices = {
            "1": self.show_tasks,
            "2": self.add_task,
            "3": self.edit_task,
            "4": self.earse_task,
            "5": self.mark_task,
            "6": self.quit,
        }

    def display_menu(self):
        print("""
            Notebook Menu
            
            1) show all tasks
            2) add task
            3) edit task
            4) earse task
            5) mark task
            6) quit            
              """)

    def show_tasks(self):
        tasks: list[Task] = self.todo.tasks

        for task in tasks:
            print(f"{task.id}: {task.name} {'❌' if not task.done else '✅'}")

    def add_task(self):
        name = input("Enter name of task: ")
        self.todo.add_task(name)

    def edit_task(self):
        id = int(input("Enter id of task: "))
        new_name = input("Enter name of new task: ")
        self.todo.modify_task(id, new_name)

    def earse_task(self):
        id = int(input("Enter of task you want to earse: "))
        self.todo.delete_task(id)

    def mark_task(self):
        id = int(input("Enter id of task you want to mark its done: "))
        self.todo.mark_task(id)

    def quit(self):
        print("Thanks for using todo app. ❤️")
        exit(0)

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter option (1, 2, 3, 4, 5, 6): ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Not valid option.")


if __name__ == "__main__":
    Menu().run()
