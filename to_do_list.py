class ToDo:
    year = 2026  
    def __init__(self, task, submit_on):
        self.task = task
        self.submit_on = submit_on

    
td1=ToDo("Homework","5 June 2026")
print(td1.task)
print(td1.submit_on)

