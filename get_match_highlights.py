api_key = "AIzaSyBtfyFYMTFiCg6J9XgxZR4l0HVVrENPMMs"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)
# print(type(youtube))
import urllib.request
import json
import datetime
from datetime import date
import maya

with open('final_matches.txt', 'r') as f:
    data = f.readlines()
    diff = 2
    for entry in  data:
        li = list(entry.split(','))
        league_name = li[0].replace('[', '')
        match = li[1]
        req = youtube.search().list(q=match + ' highlights', part='snippet', type='video',
                maxResults=10)
        # print(type(req))
        res = req.execute()
        print(len(res['items']))
        your_json = res['items']
        publishedAt = your_json[0]['snippet']['publishedAt']
        curDate = datetime.datetime.utcnow().isoformat() + "Z"
        dt_1 = maya.parse(publishedAt).datetime()
        dt_2 = maya.parse(curDate).datetime()

        print(dt_2 - dt_1)
