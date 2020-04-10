import os
from werkzeug.utils import secure_filename
# ALLOWED_EXTENSIONS = {'mp4', 'mov', 'wmv', 'avi', 'flv'}

# // VERIFICAÇÃO DE EXTENSÃO DO ARQUIVO @ A FAZER
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def salvar(app, arquivo):
    ##### Configurações do Flask/app #####
    app.config['UPLOAD_FOLDER'] = os.getcwd()+"\\uploads\\"
    arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(arquivo.filename)))