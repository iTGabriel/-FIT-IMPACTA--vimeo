import vimeo
import os

chaves = {
    'token':'19ce383ca82104a1dc87ad12dd1be1c2',
    'key':'ff8426ddae0857713c1aa93d86a90a5e78c89734',
    'secret':'nA2wNJjkOeubrQ/d2PayBxo5a1OSX2UCQpOWZmHfBnNTCTWCpltR4KaRfTRomKBVHWOE90Q28B/+KOk87cOOByOHfBrWyltVVMMr50GzPVzo239HBBcz17O1xnylGpMR'
}

vimeo_client = vimeo.VimeoClient(
  token= chaves['token'],
  key= chaves['key'],
  secret= chaves['secret']
)

# // PEGA TODOS OS VÍDEOS CONTIDOS NA CONTA
def get_all():
    return vimeo_client.get('https://api.vimeo.com/users/111831013/videos').json()

def get_id(video_id):
    print(video_id)
    return vimeo_client.get('https://api.vimeo.com/videos/'+video_id).json()

# // REALIZA UPLOAD DO VÍDEO SELECIONADO PARA A CONTA
def upload(video, dados):
    os.chdir(os.getcwd()+'\\uploads\\')
    return vimeo_client.upload(video, data=dados)
    # os.remove(video)

