from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import client_vimeo
from services.util import save_file

app = Flask(__name__)

# print(client_vimeo.get_id('406105527'))


@app.route('/')
def index():
    dados_videos = client_vimeo.get_all()
    return render_template('index.html',  message=None, videos = dados_videos['data'])

@app.route('/video', methods=['GET'])
def video():
    video_id = request.args.get('video')
    video_id = video_id.split('/')[2]
    dados_video = client_vimeo.get_id(video_id)
    link_iframe = dados_video['embed']['html'].split(' ')[1].split('src=')[1].replace('"', '')
    return render_template('player/video.html', iframe = link_iframe)




@app.route('/upload', methods=['POST', 'GET'])
def upload():
    titulo = request.form['title_video']
    descricao = request.form['describle_video']
    arquivo = request.files['file_video']
    dados = {'name':titulo, 'description': descricao}
    
    try:
        # save_file.salvar(app, arquivo)
        # client_vimeo.upload(arquivo.filename, dados)
        message = "Vídeo Enviado com sucesso"
    except:
        message = "Falha ao realizar envio do vídeo"

    return render_template('index.html', message=message)


app.run('127.0.0.1', 8000)

    # return "up"
