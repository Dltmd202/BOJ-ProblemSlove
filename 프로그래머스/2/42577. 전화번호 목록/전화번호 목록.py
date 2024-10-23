def solution(phone_book):
    answer = True
    
    hash = {}
    for pn in phone_book:
        hash[pn] = True
    
    for pn in phone_book:
        prefix = ''
        for number in pn[:-1]:
            prefix += number
            if prefix in hash:
                return False
    return True
            
    
    return answer