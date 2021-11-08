import mysql.connector
import time
from prettytable import PrettyTable

def connectdb():
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
def showtableval():
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    y=curzor.execute("select * from task")
    x=curzor.fetchall()
    for i in x:
        print(i)
    curzor.execute("select Count(*) from task")
    print(curzor.fetchall())
def insert(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon):
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon)
    curzor.execute(command, data)
    db.commit()
def deleterow(taskid):
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    command=("delete from task where taskid=%s"%(taskid))
    data=(taskid)
    curzor.execute(command,data)
    db.commit()
    time.sleep(2)
    print("Deleted Successfully..")
    showtableval()

def prioritize(priority,taskid):
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    #db,curzor=connectdb()
    print("Prioritizing the tasks......")
    time.sleep(1)
    curzor.execute("update task set priority=%s where taskid=%s",(priority,taskid))
    db.commit()
    print("Successfully set the priority.\ntaskid:"+str(taskid)+"-->priority:"+str(priority))
    showtableval()

def addbooknotes(notes,bookmark,taskid):
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    #db,curzor = connectdb()
    print("Adding Notes and Bookmarks")
    time.sleep(1)
    curzor.execute("UPDATE task SET notes=%s,bookmark=%s WHERE taskid=%s",(notes,bookmark,taskid))
    db.commit()
    print("Successfully added notes,bookmarks. ")
    showtableval()

def searchtasks(taskid):
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    print("searching the Tasks.......")
    time.sleep(2)
    command=("select taskname from task where taskid=%s"%(taskid))
    data=(taskid)
    curzor.execute(command,data)
    x=str(curzor.fetchall())
    time.sleep(1)
    t=PrettyTable(['Task Name'])
    t.add_row([x[3:len(x)-4]])
    print(t)

def trackcomp():
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    print("COMPLETED TASKS")
    curzor.execute("select taskname,taskid from task where stats='completed'")
    x=curzor.fetchall()
    t=PrettyTable(['Taskname','Task ID'])
    for i in x:
        t.add_row([i[0],i[1]])
    print(t)

def insert(tk):
    #db,curzor = connectdb()
    db = mysql.connector.connect(host="localhost", user="root", password="Qwer$600", database="casestudy")
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (tk.taskid, tk.taskname, tk.description, tk.status, tk.priority,tk.notes,tk.bookmark,tk.ownerid,tk.creatorid,tk.createdon,tk.modifiedon)
    curzor.execute(command, data)
    db.commit()
    time.sleep(2)
    print("Inserted Successfully..")
    showtableval()
