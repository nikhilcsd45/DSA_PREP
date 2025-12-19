
def sumSubarrayMins(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    MOD = 10**9 + 7
    l = len(arr)
    if l == 0:
        return 0
    leftcoverage=[0]*l
    st=[]
    for i in range(l): #[3,2,1,4,0]
        count=1
        while st and st[-1][0]>arr[i]:
            count+=st.pop()[1]

        st.append((arr[i],count))
        leftcoverage[i]=count
    
    st=[]
    rightcoverage=[0]*l
    for j in range(l-1,-1,-1):
        count=1
        while st and st[-1][0]>=arr[j]:
            count+=st.pop()[1]
        st.append((arr[j],count))
        rightcoverage[j]=count
    s=0
    for k in range(l):
        s=(s+arr[k]*(leftcoverage[k]*(rightcoverage[k])))%MOD
    return s


        


        