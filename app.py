from gtts import gTTS  
from playsound import playsound  
from flask import Flask, json, render_template, request, make_response, session, redirect, url_for, flash, abort, jsonify, send_file, Response
from mysql.connector.utils import read_bytes
import os, sys
from docxtpl import DocxTemplate, InlineImage
from DateTime import DateTime
from datetime import datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment
import mysql.connector
from docx.shared import Mm
from flask_cors import CORS
import io
import base64
from PIL import Image
import json

app = Flask(__name__)
CORS(app)
app.secret_key = 'randomterserah'

# upload gambar
app.config['UPLOAD_FOLDER'] = 'static'

mydb = mysql.connector.connect(
    host="localhost",
    user="nandapro_nawitamu",
    password="nawi_bukutamu",
    database="nandapro_bukutamu"
)

mycursor = mydb.cursor(buffered=True)

@app.route('/', methods=['GET', 'POST'])
def coba():
    
    return render_template('index.html')

@app.route('/tamu', methods=['GET', 'POST'])
def handleTamu():
    
    if request.method == 'POST':
        req = request
        kode = req.form['kode']
        nama = req.form['name']
        email = req.form['email']
        nik = req.form['nik']
        nohp = req.form['nohp']
        keperluan = req.form['keperluan']
        alamat = req.form['alamat']
        tgl = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        foto = base64.b64decode(req.form['foto']) if req.form['foto'] else None
        ttd = base64.b64decode(req.form['ttd']) if req.form['ttd'] else None
        
        sql = "INSERT INTO bukutamu (nama, datetime, email, nik, nohp, keperluan, alamat, ttd, foto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nama, tgl, email, nik, nohp, keperluan, alamat, ttd, foto)
        mycursor.execute(sql, val)

        mydb.commit()
        
        return render_template('success.html', file=kode)
    
@app.route('/ptsp', methods=['GET', 'POST'])
def ptsp():
    return render_template('ptsp.html')

@app.route('/bukutamu/<kode>', methods=['GET', 'POST'])
def bukutamu(kode):
    print(kode)
    return render_template('bukutamu.html', kode=kode)

@app.route('/texttoaudio', methods=['GET', 'POST'])
def texttoaudio():
    if request.method == 'POST':
        req = request
        
        language = 'id'
        
        kode = req.form['kode']
        text = req.form['text']
        
        obj = gTTS(text=text, lang=language, slow=False)
        obj.save("./static/assets/sound/"+kode+".mp3")
        
        return render_template('success.html', file=kode)
    
    return render_template('uploadsound.html')

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# text_val = "2022 hanya tinggal menghitung hari. Mungkin kamu bisa memberikan kata-kata bijak berkelas kepada orang-orang terdekat yang bisa memotivasi mereka agar lebih baik di 2022. 40 Kata-kata Bijak Berkelas yang Bisa Jadi Motivasi di 2022" 
# language = 'id' 
# obj = gTTS(text=text_val, lang=language, slow=False)   
# obj.save("exam.mp3")  
# playsound("exam.mp3")  