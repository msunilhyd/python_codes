with open('final_matches.txt', 'r') as f:
    data = f.readlines()
    for entry in  data:
        li = list(entry.split(','))
        league_name = li[0].replace('[', '')
        match = li[1]
