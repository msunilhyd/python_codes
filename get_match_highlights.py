# api_key = "AIzaSyBtfyFYMTFiCg6J9XgxZR4l0HVVrENPMMs"


api_key = "AIzaSyD1h5Z_oHdc4F9-jKsVDHutdpbo45iz6xc"

from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)
# print(type(youtube))
import urllib.request
import json
import datetime
from datetime import date
import maya
import webbrowser

with open('final_matches.txt', 'r') as f:
    data = f.readlines()
    print(data)
    diff = 2
    for entry in data:
        print('Hello')
        li = list(entry.split(','))
        print('li.lentgh is ', len(li))
        league_name = li[0].replace('[', '')
        print('league_name = ' + league_name)
        for i in range(1, len(li)):
            match = li[i]
            print(match)
            req = youtube.search().list(q=match + ' highlights', part='snippet', type='video',
                    maxResults=3)
            res = req.execute()
            your_json = res['items']
            publishedAt = your_json[0]['snippet']['publishedAt']
            curDate = datetime.datetime.utcnow().isoformat() + "Z"
            dt_1 = maya.parse(publishedAt).datetime()
            dt_2 = maya.parse(curDate).datetime()
    
            diff_days = str((dt_2 - dt_1)).split(',')[0]
            
            print('diff_days' + diff_days)
            if('day' in diff_days):
                diff_days = diff_days.replace(' days', '').replace(' day', '')
            else :
                diff_days = 1
            if (int(diff_days) <= 2): # need to change this to 2 as the script runs on the next day of the match
                videoId =  your_json[0]['id']['videoId']
                print(match)
                print(videoId)
                url = 'https://www.youtube.com/watch?v=' + videoId
                webbrowser.open(url)