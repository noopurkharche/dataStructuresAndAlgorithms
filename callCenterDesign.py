from abc import ABC, abstractmethod

class CallHandler:
    levels = 3
    employees = []
    callQueues = [] # this is queue for assigning the calls

    # constructor for callHandler
    def __init__(self, rank):
       pass
    
    # gets first available employee who can handle this call
    def getHandlerForCall(self, call):
        pass
    
    # routes the call to available employee or saves in queue if no employee is avauilable
    def dispatchCall(self, caller):
        call = Call(caller)
        dispatchCaller(call)
    
    def dispatchCaller(self,call):
        emp  = getHandlerForCall()
         if emp != None:
             emp.receieveCall(call)
             call.setHandler(emp)
        else:
            call.reply("Please wait for employee to be free to reply")
            callQueues.add(call)
    
    def assignCall(self,emp):
        pass
    
class Call:
    rank = None
    caller = None
    handler = None
    
    # constructor for Call
    def __init__(self, rank):
        self.caller = self
        self.rank = rank
        
    # set employee who is handling the call 
    def setHandler(self, employee):
        self.handler = employee
    
    def reply(self, message):
        pass
    
    def getRank(self):
        return rank
        
    def setRank(self, r):
        return self.rank = r
    
    def incrementRank(self, message):
        pass
    
    def disconnect(self):
        pass

# define abstract class
class Employee(ABC):
    currentCall = None
    Rank = rank
    
    def __init__(self, handler):
        pass
    
    def receieveCall(self, call):
        pass
    
    def callCompleted(self):
        pass
    
    def escalateAndReassign(self):
        pass
    
    def assignNewCall(self):
        pass
    
    def isFree(self):
        return currentCall4 = None
        
    def getRank(self):
        return rank

class Rank(enum.Enum): 
    Director = 1
    Manager = 2
    Respondent = 3

class Director(Employee):
    def __init__(self):
        self.rank = Rank.Manager
        
class Manager(Employee):
    def __init__(self):
        self.rank = Rank.Manager

class Respondent(Employee):
    def __init__(self):
        self.rank = Rank.Respondent

    
    
