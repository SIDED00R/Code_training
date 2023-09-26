def solution(m, musicinfos):
    answer = []
    
    for musicinfo in musicinfos:
        stime, etime, title, note = musicinfo.split(",")
        shour, sminute = map(int, stime.split(":"))
        ehour, eminute = map(int, etime.split(":"))
        
        long = (ehour - shour) * 60 + (eminute - sminute)
        
        half = note.count("#")
        length = len(note) - half
        q = long // length
        r = long % length
        
        added = ""
        count = 0
        
        for step in note:
            if count == r:
                if step == "#":
                    added += "#"
                break
                
            if step != "#":
                count += 1
            added += step
                    
        note = note * q + added
        
        find = ""
        okay = False
        gotit = False
        
        for alp in note:
            
            find += alp
                     
            if okay and alp == "#":
                okay = False
                
            elif okay and alp != "#":
                gotit = True
                break
                
            if m == find[-len(m):]:
                okay = True
                
            if okay and m[-1] == "#":
                gotit = True
                break
        
        if gotit or okay:
            if len(answer) == 0:
                answer = [title, long]
            elif answer[1] < long:
                answer = [title, long]
            
    if len(answer) == 0:
        return "(None)"
    else:
        return answer[0]