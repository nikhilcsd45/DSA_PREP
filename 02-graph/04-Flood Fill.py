
def floodFill(self, image, sr, sc, color):
    if image[sr][sc]==color:
        return image

    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    rows=len(image)
    cols=len(image[0])

    oldcolour=image[sr][sc]
    image[sr][sc]=color
    
    def dfs(row,col):
        for dr,dc in directions:
            nrow,ncol=row+dr,col+dc
            if 0<=nrow<rows and 0<=ncol<cols and image[nrow][ncol]==oldcolour:
                image[nrow][ncol]=color
                dfs(nrow,ncol)
    dfs(sr,sc)
    return image

            
                    


            

        