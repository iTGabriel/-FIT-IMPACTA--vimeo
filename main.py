from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import client_vimeo
from services.util import save_file

app = Flask(__name__)

# print(client_vimeo.get_id('406105527'))


@app.route('/')
def index():
    dados_videos = client_vimeo.get_all()
    return render_template('index.html',  message=None, videos = dados_videos['data'])

@app.route('/video', methods=['POST', 'GET'])
def video():
    video_id = request.form['video_id']
    video_id = video_id.split('/')[2]
    dados_video = client_vimeo.get_id(video_id)
    return render_template('modals/video.html', video = dados_video)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    titulo = request.form['title_video']
    descricao = request.form['describle_video']
    arquivo = request.files['file_video']
    dados = {'name':titulo, 'description': descricao}
    
    try:
        save_file.salvar(app, arquivo)
        client_vimeo.upload(arquivo.filename, dados)
        message = "Vídeo Enviado com sucesso"
    except:
        message = "Falha ao realizar envio do vídeo"

    dados_videos = client_vimeo.get_all()

    return render_template('index.html', message=message, videos = dados_videos['data'])

@app.route('/update', methods=['POST'])
def update():
    video_id = request.form['id_video']
    titulo = request.form['title_video']
    descricao = request.form['describle_video']
    dados = {'name':titulo, 'description': descricao}
    try:
        print(client_vimeo.update(video_id, dados))
        message = 'Dados do vídeo atualizado com sucesso'
    except:
        message = "Falha ao realizar atualização dos dados do vídeo"
    
    dados_videos = client_vimeo.get_all()
    return render_template('index.html', message = message, videos = dados_videos['data'])


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    video_id = request.form['video_id'].split('/')[2]
    try:
        print(client_vimeo.delete(video_id))
        message = "Vídeo excluido com sucesso"
    except:
        message = "Falha ao realizar exclusão do vídeo"
    
    dados_videos = client_vimeo.get_all()
    return render_template('index.html', message = message, videos = dados_videos['data'])


app.run('127.0.0.1', 8000)

    # return "up"
