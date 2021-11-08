'''from dbconnection import getconnection
from service.task import *

def create_task(task):
    mydb=getconnection()
    mycursor=mydb.cursor()
    #command = "insert into task(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)" % (Task.taskid,Task.taskname,Task.descript,Task.stats,Task.priority,Task.notes,Task.bookmark,Task.ownerid,Task.creatorid,Task.createdon,Task.modifiedon)
    #command=("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    sql="inster into task(taskid,taskname,descript ,stats ,priority  ,notes ,bookmark  ,ownerid,creatorid ,createdon ,modifiedon)"
    val=(task.taskid,task.taskname,task.descript,task.stats,task.priority,task.notes,task.bookmark,task.ownerid,task.creatorid,task.createdon,task.modifiedon)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()

def assign_task(taskid,ownerid):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "update task set ownerid=%s where taskid=%s"
    val = (ownerid,taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()


def assign_priority(taskid,priority):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "update task set priority=%s where taskid=%s"
    val = (priority, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def searchtask(taskid,taskname):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "select * from task  where taskid=%s and taskname=%s"
    val = (taskname, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

def deletetask(taskid,taskname):
    mydb = getconnection()
    mycursor = mydb.cursor()
    sql = "select * from task  where taskid=%s and taskname=%s"
    val = (taskname, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

import dbconnection #module import
from service import task #from the package
import time
def run(t):#getting object as para
    print("<<<<<<<<<<<<      WELCOME TO TASK TRACKER      >>>>>>>>>>>>")
    time.sleep(2)#its just to show
    print("connecting to Database........... ")
    time.sleep(2)
    dbconnection.connectdb()#connecting db
    print("Inserting the values.....")
    time.sleep(2)#task object is created here
    print("Inserted Successfully,getting tables ready with newly inserted values....")
    time.sleep(2)
    dbconnection.showtableval()
    print("All values are commited successfully..")#showing table from dbconnect module'''

import dbconnection
from service import task
import time
from prettytable import PrettyTable
def welcome():
    t=PrettyTable(['WELCOME TO TASK TRACKER'])
    t.add_row(['Database Connection Status:Connected'])
    t.add_row([''])
    t.add_row(['USER==root          DATABASE==python'])
    print(t)

def run(op):#getting object as para
    welcome()
    if (op==1):
        taskid = 1020
        taskname = 'web'
        description = 'js'
        status = 'completed'
        priority = 2
        notes = 'some notes'
        bookmark = 'bookm1'
        ownerid = 115
        creatorid = 225
        createdon = '2021-02-03'
        modifiedon = '2021-02-14'
        tsk = task.Task(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon,modifiedon)
        dbconnection.insert(tsk)
    elif(op==2):
        print("DELETION")
        x=int(input("Enter Task id to delete: "))
        dbconnection.deleterow(x)
    elif(op==3):
        dbconnection.showtableval()
    elif(op==4):
        id=int(input("Enter taskid(Int): "))
        pr=int(input("Enter Priority(Range[1-5]): "))
        dbconnection.prioritize(pr,id)
    elif(op==5):
        id = int(input("Enter taskid(Int): "))
        note=str(input("Enter Notes to add: "))
        bm=str(input("Enter Bookmark to add: "))
        dbconnection.addbooknotes(note,bm,id)
    elif(op==6):
        id = int(input("Enter taskid(Int): "))
        dbconnection.searchtasks(id)
    elif(op==7):
        dbconnection.trackcomp()
    else:
        print("Invalid Input.\nTry again...")
        return 0
def takeinput():
    t=PrettyTable(['Select Your Choice '])
    t.add_row(['  1]Add Values           '])
    t.add_row(['  2]Delete Value         '])
    t.add_row(['  3]Display Table        '])
    t.add_row(['  4]Prioritize           '])
    t.add_row(['  5]Add Notes & Bookmarks'])
    t.add_row(['  6]Search Tasks         '])
    t.add_row(['  7]Track Completion     '])
    t.add_row(['  0]Exit/close           '])
    print(t)
    op = int(input("Enter your choice: "))
    return op




