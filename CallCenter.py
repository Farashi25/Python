from datetime import datetime
class Call(object):
    def __init__ (self,name, phoneNumber, reason):        
        self.id = id(self)
        self.name = name
        self.phoneNumber = phoneNumber
        self.reason = reason
        self. time = datetime.now()

    def display(self):
        print "call #{} from {} ({}) for'{}'".format(self.id,self.name, self.phoneNumber, self.reason, self.time)
        return self

call1 =Call('Tim','123-456','just because')
print call1
call1.display()


class CallCenter(object):
    def __init__(self):
        self.calls =[]
        self.queue = 0
    
    def add(self,name, phoneNumber,reason):
        self.calls.append(Call(name,phoneNumber,reason))
        self.queue +=1
        return self
    
    def remove(self):
        self.calls.remove(self.calls[0])
        self.queue -= 1
        return self
    
    def info(self):
        print 'the queue size is {}:'.format(self.queue)
        for calls in self.calls:
            print calls
        return self
    def removeByNumber(self, phoneNumber):
        for calls in self.calls:
            if calls.phoneNumber == phoneNumber:
                self.calls.remove(calls)
        return self

    def sortQueue(self):
        def getKey(call):
            return call.time
        self.calls=sorted(self.calls, key=getKey)
        return self

center1=CallCenter()
center1.add('Tim','123-4567','just because he likes').add('minh', '123-4568', 'just because').add('Farashi', '701-3444','just because she hates')
center1.removeByNumber('701-3444').info()
center1.sortQueue().info()