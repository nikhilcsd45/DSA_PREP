
def asteroidCollision(self, asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    st=[]
    for aster in asteroids:
        while st and aster<0<st[-1]:
            if abs(aster)>st[-1]:
                st.pop()
                continue
            elif abs(aster)==st[-1]:
                st.pop()
            break

        else:
            st.append(aster)
    return st

    