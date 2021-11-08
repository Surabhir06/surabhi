
from dao import dbconnection
class Task:
    def __init__(self, taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon,
                 modifiedon):
        self.taskid = taskid
        self.taskname = taskname
        self.description = description
        self.status = status
        self.priority = priority
        self.notes = notes
        self.bookmark = bookmark
        self.ownerid = ownerid
        self.creatorid = creatorid
        self.createdon = createdon
        self.modifiedon = modifiedon
        dbconnection.insert(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid,
                         createdon, modifiedon)

