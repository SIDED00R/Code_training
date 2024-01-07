from collections import defaultdict

def solution(word, pages):
    N = len(pages)
    length = len(word)
    standard_score = [0] * N
    link_score = [0] * N
    address = {}
    link = defaultdict(list)
    url = "meta property=\"og:url\" content=\""
    out_url = "a href=\""
    
    for idx, page in enumerate(pages):
        check_og_url = ""
        my_og_url = ""
        check_link = ""
        out_link_url = ""
        out_link_urls = []
        check_word = ""
        find_my_url = False
        find_out_url = False
        find_word = 0
        
        for alp in page:
            check_og_url += alp
            check_link += alp
            
            if find_my_url:
                if alp != "\"":
                    my_og_url += alp
                else:
                    find_my_url = False
                    
            if find_out_url:
                if alp != "\"":
                    out_link_url += alp
                else:
                    out_link_urls.append(out_link_url)
                    out_link_url = ""
                    find_out_url = False
            
            if len(check_og_url) >= len(url):
                if check_og_url[-len(url):] == url:
                    find_my_url = True
                    
            if len(check_link) >= 8:
                if check_link[-8:] == out_url:
                    find_out_url = True
                    
            if alp.isalpha():
                check_word += alp
            else:
                if check_word.lower() == word.lower():
                    find_word += 1
                check_word = ""

        address[my_og_url] = idx
        standard_score[idx] = find_word
        for case in out_link_urls:
            link[my_og_url].append(case)
            
    for key, values in link.items():
        for value in values:
            if value in address:
                link_score[address[value]] += standard_score[address[key]] / len(values)
    
    max_value = -1
    max_value_idx = -1
    for i in range(N):
        if link_score[i] + standard_score[i] > max_value:
            max_value = link_score[i] + standard_score[i] 
            max_value_idx = i
    return max_value_idx