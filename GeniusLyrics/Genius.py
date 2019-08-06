import requests
import bs4
base_url = "https://api.genius.com/"
search_url = base_url + "search/"
cli_id="NQP3U7EBpW_h2ivnQlecMD92f5dUFfmiNV8drV81dQaodxiyeWjzdRVfLKVshpb2"
cli_tok="jgS62kc6s_PBjP3e0P7q7qR4lzC125MyqWWxhrLjn11o1Ndfh9cZ58wEe5IVnnRi"
header = {'Authorization':'Bearer '+ cli_tok}
def getLyric(author_name,music_title):
    if music_title == '':
        data = {'q':author_name}
    elif author_name == '':
        data = {'q': music_title}
    else:
        data = {'q':author_name + " " + music_title}
    req = requests.get(search_url, data=data,headers=header)
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

a=input("Author name")
b= input("Music name")
req = getLyric(a,b)

print(req)