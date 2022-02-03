def solution(m, n, puddles):
    arr=[[0]*m for _ in range(n)]
    arr[0][0]=1;
    for i in range(0,len(puddles)):
        arr[puddles[i][1]-1][puddles[i][0]-1]=-1;
    for i in range(0,n):
        for j in range(0,m):
            if(arr[i][j]==-1):
                arr[i][j]==0
            else:
                if(arr[i-1][j]==-1):
                    arr[i][j]+=arr[i][j-1];
                elif(arr[i][j-1]==-1):
                    arr[i][j]+=arr[i-1][j];
                else:
                    arr[i][j]+=arr[i][j-1]+arr[i-1][j];
    return arr[n-1][m-1]%1000000007;
                
        
print(solution(4,3,[[2, 2]]));