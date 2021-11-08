'''from dao import taskdao
taskid=1021
taskname='add'
description='Name'
status='completed'
priority=2
notes='no notes'
bookmark='bookm1'
ownerid=111
creatorid=211
createdon='2021-02-03'
modifiedon='2021-02-14'
tsk = taskdao.task.Task(taskid,taskname,description,status,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)
taskdao.run(tsk)'''

from service import task
from dao import taskdao
from prettytable import PrettyTable

while(1):
    x=taskdao.takeinput()
    if(x):
        taskdao.run(x)
    else:
        break
print("Exiting.....\nAll changes are commited successfully..")

