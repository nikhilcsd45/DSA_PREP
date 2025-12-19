class MinStack(object):

    def __init__(self):
        self.st=[]
        self.minst=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st.append(val)
        if len(self.minst)==0 or  val<=self.minst[-1]:
            self.minst.append(val)
        
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.st)==0:
            return -1
        temp=self.st.pop()
        if len(self.minst)>0:
            
            if temp==self.minst[-1]:
                self.minst.pop()
        return temp
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.st)==0:
            return -1
        return self.st[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minst)==0:
            return -1
        return self.minst[-1]
