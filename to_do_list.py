'''
Viết chương trình to_do_list (console app):
Yêu cầu:
Hiển thị menu task bao gồm
1 cho phép người dùng nhập task (task có 2 trạng thái là pending và done)
2 xây dụng chức năng hiển thị tất cả task
3 xây dụng chức năng tick hoàn thành task dựa trên mã task
4 xây dựng chức năng thoát
'''
from models.Task import Task

task_list = []

running = True
while running:
    print(f'''
          1/ Thêm task
          2/ Hiển thị nội dung task
          3/ Chọn task hoàn thành
          4/ Thoát
          ''')
    select = input('Chọn chức năng: ')
    if select == '1':
        new_task = Task()
        new_task.input_task()
        task_list.append(new_task)
    elif select == '2':
        for task in task_list:
            task.display()
    elif select == '3':
        task_done = input('Nhập tên task hoàn thành: ')
        for task in task_list:
            if task.task_name == task_done:
                task.status = 'done'
        for task in task_list:
            task.display()
    elif select == '4':
        running = False