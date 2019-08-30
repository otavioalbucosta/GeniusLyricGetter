import bs4
import requests
import pytube
import moviepy.editor
base_url = "https://api.genius.com/"
youtube_url = "https://www.googleapis.com/youtube/v3/search"
search_url = base_url + "search/"
cli_id="NQP3U7EBpW_h2ivnQlecMD92f5dUFfmiNV8drV81dQaodxiyeWjzdRVfLKVshpb2"
cli_tok="jgS62kc6s_PBjP3e0P7q7qR4lzC125MyqWWxhrLjn11o1Ndfh9cZ58wEe5IVnnRi"
yt_key = "AIzaSyBnrEKxA6QZ6hTuNjj4LRuk9MDdQtI8NNA"
geniusHeader = {'Authorization':'Bearer '+ cli_tok}
def getLyric(author_name,music_title):
    if music_title == '':
        data = {'q':author_name}
    elif author_name == '':
        data = {'q': music_title}
    else:
        data = {'q':author_name + " " + music_title}
    req = requests.get(search_url, data=data,headers=geniusHeader)
    req = req.json()
    i = int(1)
    print(req['response']['hits'])
    for hit in req['response']['hits']:
        print(str(i) + ': '+  hit['result']['title'] + " - " + hit['result']["primary_artist"]["name"])
        i+=1
    val = int(input("Digite a musica que deseja de acordo com o numero"))
    link = req['response']['hits'][val-1]['result']['url']
    pagereq = requests.get(link)
    text  = bs4.BeautifulSoup(pagereq.text, 'html.parser')
    lyrics = text.find('div', class_='lyrics').get_text()
    return lyrics

def searchMusic(query):

    data = {'q':query,'part':'snippet','key':yt_key}
    req = requests.get(youtube_url,params=data)
    print(req.url)
    req = req.json()
    val = 1
    for videos in req['items']:
        print(str(val) + " - " + videos['snippet']['title'])
        val+=1
    val = int(input("digite o numero do vídeo desejado\n"))
    return "http://youtube.com/watch?v=" + req['items'][val-1]['id']['videoId']

def downloadMusic(link):
    titlelnk = link.replace('http://youtube.com/watch?v=','')
    data = {'q': titlelnk, 'part': 'snippet', 'key': yt_key}
    titreq = requests.get(youtube_url,params=data)
    titreq = titreq.json()
    titreq  = titreq['items'][0]['snippet']['title']
    print(titreq)
    videos = pytube.YouTube(link).streams.filter(only_audio=True).all()
    val = 1
    for video in videos:
        print(video.itag)
        if video.mime_type == "audio/mp4":
            video.download(filename=titreq)
            break






#a=input("Author name")
#b= input("Music name")
#req = getLyric(a,b)

a = input("namaewa")
downloadMusic(searchMusic(a))
