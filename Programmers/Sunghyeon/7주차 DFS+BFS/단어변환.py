from collections import deque
def solution(begin, target, words):
    if(target not in words):
        return 0
    que=deque();
    que.append([begin,0]);
    
    while(len(que)!=0):
        tmp=que.popleft();
        if(tmp[0]==target):
            return tmp[1];
        for i in range(0,len(words)):
            cnt=0;
            if(words[i]==tmp[0]):
                continue;
            for j in range(0,len(words[i])):
                if(tmp[0][j]!=words[i][j]):
                    cnt=cnt+1;
            if(cnt==1):
                que.append([words[i],tmp[1]+1]);

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]));