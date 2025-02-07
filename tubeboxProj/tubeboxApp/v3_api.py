import requests
import json

def youtube_v3(keyword):
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=50&key=AIzaSyBs8zN6vnrCr3m4_hGxfwibR14J3agDpJA&part=statistics&pageToken"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    item_list = response_json['items']
    result_list = {}
    result_list['items'] = []
    for i in item_list:
        result_list['items'].append({
            "id": i['id'],
            "publishedAt": i['snippet']['publishedAt'],
            "title": i['snippet']['title'],
            "description": i['snippet']['description'],
            "channelTitle": i['snippet']['channelTitle'],
            #"tags": i['snippet']['tags'],
            "viewCount": i['statistics']['viewCount'],
            "likeCount": i['statistics']['likeCount'],
            "favoriteCount": i['statistics']['favoriteCount'],
            "commentCount": i['statistics']['commentCount']
            })
    return result_list
