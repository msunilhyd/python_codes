api_key = "AIzaSyBtfyFYMTFiCg6J9XgxZR4l0HVVrENPMMs"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)
# print(type(youtube))
import urllib.request
import json
import datetime
from bson.objectid import ObjectId

curDate = datetime.datetime.utcnow().isoformat() + "Z"
print(curDate)
splittedDate = curDate.split('T')
print(splittedDate[0])
date_format = "%Y-%m-%d"
a = datetime.datetime.strptime(splittedDate[0], date_format)

prev_date = datetime.datetime.today() - datetime.timedelta(days=1)
prev_date = str(prev_date).split(' ')[0]
print(prev_date, 'kdj')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['charactersDB']
characters = db['characters']
# test_date = datetime.datetime.strptime("2021-01-24", date_format)

for data in characters.find({'date': prev_date}):
    print(data, '33333')
    vid_id_list = []
    for match in data.get('match_list'):
        video_id = 'abc234d';
        print('match is ++', match)
        req = youtube.search().list(q=match + ' highlights', part='snippet', type='video',
                maxResults=10)
        # print(type(req))
        res = req.execute()
        print(len(res['items']))
        vidLength = 0
        vidIdOfInt = ''
        # print('vidOfInt length is : ',  len(vidOfInt))
        for x in res['items']:
            vidId = x['id']['videoId']
            # print(vidId, '============')
            # print(x['snippet']['title'])
            # print(x['snippet']['publishedAt'])
            publishedAt = x['snippet']['publishedAt']
            publishedAt = publishedAt.split('T')[0]
            b = datetime.datetime.strptime(publishedAt, date_format)
            delta = a - b
            # print(delta.days)
            day_difference = delta.days
            if (day_difference == 0 or day_difference == 1 or day_difference == 2):
                searchUrl = f'''https://www.googleapis.com/youtube/v3/videos?id={vidId}&key={api_key}&part=contentDetails'''
                response = urllib.request.urlopen(searchUrl).read()
                json_data = json.loads(response)
                all_data = json_data['items']
                duration = all_data[0]['contentDetails']['duration']
                # print(duration, 'duration')
                if 'M' in duration:
                    minutes = int((duration.split('M')[0])[2])
                    # print(minutes)
                    if minutes > vidLength:
                        vidLength = minutes
                        vidIdOfInt = vidId
                    # print(data)
                    # print(vidId)
        print()


        # print('Max Length is = ' , vidLength, vidIdOfInt)
        vid_id_list.append(vidIdOfInt)
    print(vid_id_list)
    new_val = {'vid_id_list': vid_id_list};
    print(new_val, '999999')
    print(data, '11111')
    print(data.get('_id'), '888888')
    print(data.get('league_name'))
    characters.update_one({"_id": ObjectId(data.get('_id'))}, {"$set": new_val})
