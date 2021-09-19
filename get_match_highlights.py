api_key = "AIzaSyBtfyFYMTFiCg6J9XgxZR4l0HVVrENPMMs"
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
    diff = 2
    for entry in  data:
        li = list(entry.split(','))
        league_name = li[0].replace('[', '')
        match = li[1]
        req = youtube.search().list(q=match + ' highlights', part='snippet', type='video',
                maxResults=10)
        res = req.execute()
        your_json = res['items']
        publishedAt = your_json[0]['snippet']['publishedAt']
        curDate = datetime.datetime.utcnow().isoformat() + "Z"
        dt_1 = maya.parse(publishedAt).datetime()
        dt_2 = maya.parse(curDate).datetime()

        diff_days = str((dt_2 - dt_1)).split(',')[0]
        diff_days = diff_days.replace(' days', '')
        print(diff_days)
        if (int(diff_days) <= 3): # need to change this to 2 as the script runs on the next day of the match
            videoId =  your_json[0]['id']['videoId']
            print(videoId)
            url = 'https://www.youtube.com/watch?v=' + videoId
            webbrowser.open(url)