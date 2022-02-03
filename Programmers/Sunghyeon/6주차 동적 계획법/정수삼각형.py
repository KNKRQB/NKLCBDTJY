def solution(triangle):
    list= []
    for i in range(0,len(triangle)):
        triangle[i].insert(0,0);
        triangle[i].append(0);
        
    for i in range(0,len(triangle)):
        tmp = [0 for i in range(len(triangle[i]))];
        list.append(tmp);
        
    list[0][1]=triangle[0][1];
    for i in range(0,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            tmp=max(list[i-1][j-1],list[i-1][j]);
            list[i][j]=tmp+triangle[i][j];
    return max(list[len(list)-1])
    
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));