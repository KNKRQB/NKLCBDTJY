def solution(routes):
    prev=-40000;
    ans=0;
    routes.sort(key=lambda x:x[1]); 
    print(routes);
    
    for i in routes:
        if prev<i[0]:
            ans=ans+1
            prev=i[1];
            
    return ans;

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]));

# https://dev-note-97.tistory.com/125