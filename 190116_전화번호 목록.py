def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    answer = True
    for i, phone1 in enumerate(phone_book):
        hash_map = {}
        for phone2 in phone_book[i+1:]:
            hash_map[phone2[:len(phone1)]] = phone2
        if phone1 in hash_map:
            answer = False
            break
    return answer

