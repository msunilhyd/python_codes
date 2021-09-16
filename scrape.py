import requests
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)
import datetime

curDate = datetime.datetime.utcnow().isoformat() + "Z"
print(curDate)
splittedDate = curDate.split('T')
print(splittedDate[0])

actual_url = "https://www.sportinglife.com/football/fixtures"
page = requests.get(actual_url)
# print(page.content)

from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
# print(list(soup.children))

# print([type(item) for item in list(soup.children)])

# html = list(soup.children)[2]
# print(list(html.children))
# body = list(html.children)[3]
# p = list(body.children)[1]
# print(p.get_text())

print("Hello World")
# f = open("/home/sunil/Desktop/ytAPI/footballTwo.html", "r")
# content = f.read()
content = page.content
print("_______________")

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
mylis = soup.find_all("li", {"class": "FootballLiveCompetitionList__CompetitionListItem-sc-112crmw-1 dRylsD"})
print(len(mylis))

class LeagueObject:
    def __init__(self, league_name, match_list):
        self.league_name = league_name
        self.match_list = match_list
        self.date = splittedDate[0]

    def __str__(self):
        return ' League: ' + self.league_name + '\n matches: \t'+ str(self.match_list) + ' '+str(self.date)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['charactersDB']
characters = db['characters']

league_objects_list = []
league_list_of_interest = ['English Premier League',
'Spanish Copa Del Rey',
'Portuguese Primeira Liga',
'Turkish Super Lig',
'Coppa Italia',
'FRENCH LIGUE 1',
'Spanish La Liga',
'German Bundesliga',
'Italian Serie A']
for lis in mylis:
    # company_names = lis.find_all('span', {"class": "CompactText__DataCompactText-sc-1rtlz3k-0 jdvCWg"})
    # print(lis)
    league_title = lis.find('h3', {"class": "ContentPanel__ContentPanelTitle-sc-1izwmji-1"})
    # print(league_title.text)
    company_names_first = lis.find_all('span', {"class": "FootballMatchListItem__TeamA-sc-9lgblw-6"})
    company_names_second = lis.find_all('span', {"class": "FootballMatchListItem__TeamB-sc-9lgblw-8"})


    # print(len(company_names_first))
    # print(len(company_names_second))
    match_list = []
    for i in range(0, len(company_names_first)):
        match_list.append(company_names_first[i].text + ' vs '+ company_names_second[i].text)
        print(match_list, '----')
    league_object = LeagueObject(league_title.text, match_list)

    print(league_object)
    if league_object.league_name in league_list_of_interest:
        print('present 3333')
        key = {'league_name': league_title.text, 'date': league_object.date }
        characters.update_one(key, {"$set": league_object.__dict__}, upsert=True)
        print("+++++++++++++++")
        print(league_object.__dict__)

print('000000000000')

# print(league_objects_list)

# db.characters.aggregate([ { $group : {_id: "$gender", result: {$sum: 1 } } } ]);
