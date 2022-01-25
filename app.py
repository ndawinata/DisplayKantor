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

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="nandapro_nawi",
#     password="nawi_seismonapp",
#     database="nandapro_seismon"
# )

# mycursor = mydb.cursor(buffered=True)

@app.route('/', methods=['GET', 'POST'])
def coba():
    # playsound("exam.mp3")
    
    return render_template('index.html')

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