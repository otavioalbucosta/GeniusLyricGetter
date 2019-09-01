import bs4
import requests
import pytube
import subprocess
import os


## Tokens and base links ##
genius_url = "https://api.genius.com/"
youtube_url = "https://www.googleapis.com/youtube/v3/search"
search_url = genius_url + "search/"
cli_tok="jgS62kc6s_PBjP3e0P7q7qR4lzC125MyqWWxhrLjn11o1Ndfh9cZ58wEe5IVnnRi"
yt_key = "AIzaSyBnrEKxA6QZ6hTuNjj4LRuk9MDdQtI8NNA"
geniusHeader = {'Authorization':'Bearer '+ cli_tok}




def getLyric(search):
    data = {'q':search}
    req = requests.get(search_url, data=data, headers=geniusHeader)
    req = req.json()
    i = int(1)
    print(req['response']['hits'])
    for hit in req['response']['hits']:
        print(str(i) + ': ' + hit['result']['title'] + " - " + hit['result']["primary_artist"]["name"])
        i += 1
    val = int(input("Digite a musica que deseja de acordo com o numero"))
    link = req['response']['hits'][val-1]['result']['url']
    pagereq = requests.get(link)
    text = bs4.BeautifulSoup(pagereq.text, 'html.parser')
    lyrics = text.find('div', class_='lyrics').get_text()
    return lyrics

def listMusic(query):
    data = {'q': query, 'part': 'snippet', 'key': yt_key, }
    req = requests.get(youtube_url, params=data)
    req = req.json()
    val = 1
    listmus =[]
    for videos in req['items']:
        listmus.append(str(val) + " - " + videos['snippet']['title'])
        val+=1
    return listmus
def getMusic(query, val):

    data = {'q': query, 'part': 'snippet', 'key': yt_key, }
    req = requests.get(youtube_url,params=data)
    req = req.json()
    return "http://youtube.com/watch?v=" + req['items'][val-1]['id']['videoId']


def downloadMusic(link):

    titlelnk = link.replace('http://youtube.com/watch?v=','')
    data = {'q': titlelnk, 'part': 'snippet', 'key': yt_key}
    titreq = requests.get(youtube_url,params=data)
    titreq = titreq.json()
    titreq  = titreq['items'][0]['snippet']['title']
    videos = pytube.YouTube(link).streams.filter(only_audio=True).all()
    for video in videos:
        print(video.itag)
        if video.mime_type == "audio/mp4":
            video.download("/Songs",filename=titreq)
            convert_video("/Songs/"+titreq+'.mp4','/Songs/'+titreq+".mp3")
            os.remove("/Songs/"+titreq + '.mp4')
            break
    return titreq+".mp3"


def convert_video(video_input, video_output):

    cmds = ['ffmpeg', '-i', video_input, video_output]
    subprocess.Popen(cmds).wait()

