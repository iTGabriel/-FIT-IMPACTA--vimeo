import os
from werkzeug.utils import secure_filename

def salvar(app, arquivo, caminho):
    ##### Configurações do Flask/app #####
    app.config['UPLOAD_FOLDER'] = caminho+"\\uploads\\"
    arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(arquivo.filename)))