from re import I
import requests
from bs4 import BeautifulSoup

# data = requests.get('https://www.sportinglife.com/football/fixtures').text
# with open('data.html', 'w') as f:
#     f.write(data)

with open('data.html', 'r') as f:
    html_text = f.read()
    soup = BeautifulSoup(html_text, 'lxml')
    leagues = soup.find_all('div', class_ = 'CompetitionList__FootballMatchList-sc-1f2woz6-2 jAWlfM')

    for index, league in enumerate(leagues):
        print()
        league_name = league.find('h3', class_ = 'ContentPanel__ContentPanelTitle-sc-1izwmji-1 fyrfui ContentPanel__ContentPanelTitle-sc-1izwmji-1 fyrfui').text
        print(league_name)
        matches = league.find_all('div', class_ = 'Item__TeamScores-et8305-5 ehEtxo')
        for match in matches:
            teamA = match.find_all('span', class_ = 'Item__TeamA-et8305-6 jqhoIZ')
            teamB = match.find_all('span', class_ = 'Item__TeamB-et8305-8 fFHtPs')
            football_match = teamA[0].text + ' vs ' + teamB[0].text 
            print(football_match)
