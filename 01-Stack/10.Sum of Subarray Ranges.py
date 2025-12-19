
def subArrayRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # min contribution 
    l=len(nums)
    st=[]
    leftcoverage=[0]*l
    for i in range(l):
        count=1
        while st and st[-1][0]>nums[i]:
            count+=st.pop()[1]
        st.append((nums[i],count))
        leftcoverage[i]=count
    st=[]
    rightcoverage=[0]*l
    for i in range(l-1,-1,-1):
        count=1
        while st and st[-1][0]>=nums[i]:
            count+=st.pop()[1]
        st.append((nums[i],count))
        rightcoverage[i]=count
    
    #max contribution 
    st=[]
    rightmaxcoverage=[0]*l 
    for i in range(l-1,-1,-1):
        count=1
        while st and st[-1][0]<nums[i]:
            count+=st.pop()[1]
        st.append((nums[i],count))
        rightmaxcoverage[i]=count
    st=[]
    leftmaxcoverage=[0]*l
    for i in range(l):#[3,2,1,4,0]
        count=1
        while st and st[-1][0]<=nums[i]:
            count+=st.pop()[1]
        st.append((nums[i],count))
        leftmaxcoverage[i]=count
    
    total=0
    for i in range(l):
        total+=nums[i]*(leftmaxcoverage[i]*rightmaxcoverage[i]-leftcoverage[i]*rightcoverage[i])
    
    return total
    
    
    