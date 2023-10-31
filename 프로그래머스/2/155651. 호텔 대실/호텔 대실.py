def solution(book_time):
    rooms = []
    book_time = sorted(book_time, key = lambda x: x[0], reverse = True)
    while book_time != []:
        time = book_time.pop()
        h1, m1 = map(int, time[0].split(":"))
        h2, m2 = map(int, time[1].split(":"))
        if rooms == []:
            rooms.append(h2 * 60 + m2 + 10)
        else:
            able = False
            for i, room in enumerate(rooms):
                if room <= h1 * 60 + m1:
                    able = True
                    idx = i
                    break
            if able:
                rooms[idx] = h2 * 60 + m2 + 10
            else:
                rooms.append(h2 * 60 + m2 + 10)
    
    return len(rooms)