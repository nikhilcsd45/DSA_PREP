import operator
def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    

    op_map = {
        "*": operator.mul,
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv
    }

    st=[]
    s={"+","-","*","/"}
    for i in tokens:
        if i in s:
            lstnum=st.pop()
            seclstnum=st.pop()
            temp=op_map[i](int(seclstnum),int(lstnum))
            st.append(temp)
        else:
            st.append(i)
        
    return int(st[0])