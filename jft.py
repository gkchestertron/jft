from flask import Markup
import re
import os

def templates(path):
    """
    templates need to have a .jft extension
    you must also have a /assets/js/templates/ folder
    """
    path_base = './assets/js/templates/'
    file_pr = re.compile('.*jft$')
    folder_pr = re.compile('[^.]')

    files     = [f for f in os.listdir(path_base + path)]
    response  = {}
    
    for f in files:
        if file_pr.match(f):
            file        = open(path_base + path + f)
            response[path + f[:-4:]] = file.read()
            file.close()
        elif (folder_pr.match(f)):
            response.update(templates(f + '/'))

    return response

def init(app):
    app.jinja_env.globals['JFT'] = Markup('<script>window.JFT = {0};</script>'.format(str(templates(''))))
