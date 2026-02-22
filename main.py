import json
import os 
from datetime import datetime


class Task:
    def__init__(self, title, description, priority):
       self.title = title 
       self.description = description
       self.priority = priority
       self.completed = False
       self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return{
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["description"], data["priority"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task
    
    class TaskManager:
        def__init__(self, filename="tasks.json"):
        self.filname = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print("Task adăugat cu succes!")
        
    def delete_task(self, index):
      if 0<= index < len(self.tasks):
        del self.tasks[index]
        self.save_tasks()
        print("Task șters cu succes!")
      else:
        print("Index invalid!")
    
    def mark_completed(self, index):
      if 0 <= index < len(self.tasks):
        self.tasks[index].completed = True
        self.save_tasks()
        print("Task marcat ca finalizat!")
      else:
        print("Index invalid!")

    def show_tasks(self,filter_type=None):
       if not self.tasks:
          print("Nu există task-uri.")
          return
       
       for i, task in enumerate(self.tasks):
          if filter_type == "completed" and not task.completed:
              continue
          if filter_type == "pending" and task.completed:
              continue
          
          status = "✔" if task.completed else "✘"
          print(f"\nIndex: {i}")
          print(f"TITLU: {task.title}")
          print(f"Descriere: {task>description}")
          print(f"Print: {task.priority}")
          print(f"Status: {status}")
          print(f"Creat la: {task.created_at}")

    def save_tasks(self)
        with open(self.filname, "w") as f:
            json.dump([task.to_dicg() for task in self.tasks], f, indent=4)
        
    def load_tasks(self):
        if os.path.exists(self.filname):
            with open(self.filename, "r") as f:
               data = json.load(f)
               self.tasks = [Task.from_dict(task) for task in data]

    def clear_screen():
        os.system("cls" if os.name == "nt" else " clear")


    def main_menu():
        manager = TaskManager()

    