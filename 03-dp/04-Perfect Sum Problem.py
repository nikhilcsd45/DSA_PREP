def perfectSum(self, arr, target):
	    
    l=len(arr)
    dp=[[-1]*(target+1) for _ in range(l+1)]
    
    def f(i,t):
        if i==0:
            if t==0 and arr[i]==0:
                
                return 2
            if t==0 or arr[i]==t:
                return 1
            
            return 0
        
        if dp[i][t]!=-1:
            return dp[i][t]
        
        pick=0
        if arr[i]<=t:
            pick=f(i-1,t-arr[i])
        notpick=f(i-1,t)
        
        dp[i][t]=pick+notpick
        
        return dp[i][t]
        
    return f(len(arr)-1,target)
	    
	    
	    
	    
		          
		    
		    
		       
		  
		  
		  
		  
		      
	   
		      
		        
		    
		   
		    
		