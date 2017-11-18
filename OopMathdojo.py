# from arithmetic import add, subtract
class MathDojo(object):
    def __init__(self, *start):
        self.start = 0


    def add(self, *start):
        for i in range(0, len(start)):
            if isinstance (start[i],list):
                for j in start[i]:
                    self.start += j 
            else:
                self.start += start[i]
        return self
    
    def subtract(self, *start):
        for i in range(0, len(start)):
            if isinstance (start[i],list):
                for j in start[i]:
                    self.start -= j 
            else:
                self.start -= start[i]
        return self
    
    
    def displayinfo(self):
        print self.start
   
    

    
mathdojo = MathDojo(2)
mathdojo.add([1],3,4).add([3,5,7,8],[2, 4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).displayinfo()

# if instance (start,list) or (start, tuple):