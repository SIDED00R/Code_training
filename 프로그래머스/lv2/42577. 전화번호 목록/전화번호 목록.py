def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for idx in range(len(phone_book) - 1):
        if len(phone_book[idx]) < len(phone_book[idx + 1]):
            if phone_book[idx] == phone_book[idx + 1][:len(phone_book[idx])]:
                return False
            
    return True