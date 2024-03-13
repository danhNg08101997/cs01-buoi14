class Task:
    def __init__(self) -> None:
        self.task_name = ''
        self.status = 'pending'
        
    def input_task(self):
        self.task_name = input('Nhập tên task: ')
        self.status = 'pending'
        
    def display(self):
        print(f'''
              {self.task_name} - {self.status}
              ''')