import json
import os 
from datetime import datetime


class Task:
    def __init__(self, title, description, priority):
        self.title = title 
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def    to_dict(self):
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
        def __init__(self, filename="tasks.json"):
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
          print(f"Descriere: {task.description}")
          print(f"Prioritate: {task.priority}")
          print(f"Status: {status}")
          print(f"Creat la: {task.created_at}")

    def save_tasks(self):
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

        while True:
           print("\n===== TASK MANAGER =====")
           print("1. Adaugă task")
           print("2. Șterge task")
           print("3. Marchează task ca finalizat")
           print("4. Afișează toate task-urile")
           print("5. Afișază toate task-uri finalizate")
           print("6. Afișează task-uri nefinalizate")
           print("7. Ieșire")

           choice = input("Alege o opțiune: ")

           if choice == "1":
              title = input("Titlu: ")
              description = input("Descriere: ")
              priority = input("Prioritate (Low/Medium/High): ")
              manager.add_task(title, description, priority)

           elif choice == "2":
               manager.show_tasks()    
                try:                
                    index = int(input("Index task de șters: "))
                    manager.mark_completed(index)
                except ValueError:
                    print("Introdu un număr valid!")

            elif choice =="3":
                manager.show_tasks()
                try:                
                   index =int(input("Index task de marcat: "))
                   manager.mark_completed(index)
                except ValueError:
                   print("Introdu un număr valid!")

            elif choice == "4":
                manager.show_tasks()

            elif choice == "5":
                manager.show_tasks(filter_type="completed")

            elif choice == "6":
                manager.show_tasks(filter_type="pending")

            elif choice == "7":
              print("La revedere!")
              break
            
            else:
              print("Opțiune invalidă!")

            input("\nApasă Enter pentru a continua...")
            clear_screen()

if__name__ == "__main__":
   main_menu()