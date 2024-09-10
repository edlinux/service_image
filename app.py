
from flask import Flask, request
import base64
import datetime
from datetime import datetime
from pathlib import Path
import os

app = Flask(__name__)

@app.post("/foto_display")
def add_foto():
    if request.method == 'POST':
        destino = 'images'
        img_bytes = request.get_json()['image']
        img_utf8 = img_bytes.encode('utf-8')
        img_base64 = base64.b64decode(img_utf8)
        id= request.get_json()['id']
        name= request.get_json()['name']
        dia_atual = datetime.now().strftime('%Y-%m-%d')
        if not Path(f'{destino}/{id}').is_dir():
            os.mkdir(f'{destino}/{id}')
        if not Path(f'{destino}/{id}/{dia_atual}').is_dir():
            os.mkdir(f'{destino}/{id}/{dia_atual}')
        arquivo = f'{destino}/{id}/{dia_atual}/{name}.png'
        with open(arquivo, 'wb') as file_to_save:
             file_to_save.write(img_base64)
    return 'OK'
if __name__ == '__main__':
   app.run(host="0.0.0.0",port=6000, threaded=True, debug=True)