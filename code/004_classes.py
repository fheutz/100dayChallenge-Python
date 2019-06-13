import json
import datetime

class Idea:
    """Idea Object"""
    name = "noNameSpecified"
    def __init__(self, name, predecessors=[], successors=[], tags=[]):
        self.name = name
        self.predecessors = []
        self.successors = []
        self.tags = []
        for pre in predecessors:
            self.addPredecessor(pre)
        for suc in successors:
            self.addSuccessor(suc)
        self.tags.extend(tags)
        self.created = datetime.datetime.now()
        self.changed = datetime.datetime.now()

    def addPredecessor(self, predecessor):
        if(isinstance(predecessor, Idea)):
            predecessor.successors.append(self)
            self.predecessors.append(predecessor)
        else:
            print("error predecessor is not an Idea-Type")
        self.changed = datetime.datetime.now()

    def addSuccessor(self, successor):
        if(isinstance(successor, Idea)):
            successor.predecessors.append(self)
            self.successors.append(successor)
        else:
            print("error successor is not an Idea-Type")
        self.changed = datetime.datetime.now()

    def toJson(self):
        selfDict = {
            "name": self.name,
            "predecessors":[],
            "successors":[],
            "tags":self.tags,
            "created": self.created.strftime("%d-%m-%Y %H:%M"),
            "changed": self.changed.strftime("%d-%m-%Y %H:%M")
        }
        for pre in self.predecessors:
            selfDict["predecessors"].append(pre.name)
        for suc in self.successors:
            selfDict["successors"].append(suc.name)
        return json.dumps(selfDict, indent=4)

# Runblock
x = Idea("test", tags=["a","b"])
y = Idea("test2", tags=["a","c"])
x.addPredecessor("wrong type")
x.addPredecessor(y)

print(x.toJson())
print(y.toJson())