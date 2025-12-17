def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        star=[]

        for ind,i in enumerate(s):
            if i =="(":
                stack.append(ind)
            
            elif i==")":
                if stack :
                    stack.pop()
                
                elif star:
                        star.pop()
                else:
                    return False
            else:
                star.append(ind)

        
        while stack and star:
            if stack[-1]<star[-1]:# checking for "(" before "*"
                stack.pop()
                star.pop()
            else:
                return False

        
        return True if not stack else False
        
