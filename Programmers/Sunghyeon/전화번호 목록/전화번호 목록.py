def solution(phone_book):
    phone_book.sort();
    max=len(phone_book)-1;
    for i in range(max):
        if (phone_book[i+1].find(phone_book[i])==0):
            return False;
    return True;

print(solution(["119", "97674223", "1195524421"]));
