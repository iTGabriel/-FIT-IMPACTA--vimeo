import vimeo
import os

chaves = {
    'token':'SEU TOKEN',
    'key':'SUA CHAVE',
    'secret':'SUA CHAVE SECRETA'
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
    return vimeo_client.get('https://api.vimeo.com/videos/'+video_id).json()

# // REALIZA UPLOAD DO VÍDEO SELECIONADO PARA A CONTA
def upload(video, dados, caminho):
    os.chdir(caminho+'\\uploads\\')
    return vimeo_client.upload(video, data=dados)

def update(video_id, dados):    
    return vimeo_client.patch('https://api.vimeo.com/videos/'+video_id, data = dados)


def delete(video_id):
    return vimeo_client.delete('https://api.vimeo.com/videos/'+video_id)

