```python
def solution(phone_book):
    max=len(phone_book);
    for i in range(max):
        for j in range(i+1,max):
            if ((phone_book[i].find(phone_book[j])==0)|(phone_book[j].find(phone_book[i])==0)):
                return False;
    return True;

print(solution(["119", "97674223", "1195524421"]));
```

이렇게 코드를 작성하였으나 시간초과가 발생하였습니다.

```py
def solution(phone_book):
    phone_book.sort();
    max=len(phone_book)-1;
    for i in range(max):
        if ((phone_book[i].find(phone_book[i+1])==0)|(phone_book[i+1].find(phone_book[i])==0)):
            return False;
    return True;
```

이중for문을 순회하던 것을 파이썬 내장함수로 정렬 후에 한 번만 순회하도록 하였습니다.

sort함수의 시간 복잡도는 O(nlogn)이라고 합니다.

sort함수를 실행한 후에 배열을 한 번 순회했으므로 총 시간복잡도는 O(nlogn+n)입니다.

Big-O 표기법으로 나타내면 O(nlogn)입니다.

# ref

https://wikidocs.net/13#2index
https://wikidocs.net/22
https://wikidocs.net/104141
https://wikidocs.net/20
https://ssungkang.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%95%A8%EC%88%98-find%EC%99%80-index
https://daimhada.tistory.com/56
