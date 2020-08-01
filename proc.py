import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string
from gtts import gTTS
import docx
from docx import Document
from docx.shared import Inches
doc = docx.Document()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
src_path=r"static/uploads/"

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = { 'png','jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def main():
	return render_template("file.html")
def allowed_file(filename):
      return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_string(img_path):
       # Recognize text with tesseract for python
       result = pytesseract.image_to_string(Image.open("upload1.jpg"))
       return result 
        
   
    
    

@app.route('/img', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
          
            return render_template("file.html")

        
        if file and allowed_file(file.filename):
            os.chdir(r'C:\Users\kousik\Desktop\converto\static\uploads')
            
            file.filename="upload1.jpg"
            file.save(file.filename)
            
        return render_template("ex.html")
@app.route('/ex',methods=['GET', 'POST'])
def extract():
       # print('--- Start recognize text from image ---')
        res=get_string(src_path + "upload1.jpg") 
        #print('--- Done ---')
        myobj = gTTS(text=res, lang='en', slow=False)
        myobj.save("welcome1.mp3")
        os.system("mpg321 welcome1.mp3")
        doc.add_paragraph(res)
        doc.save('output.docx')
        return render_template("res.html",data=res)
    

if __name__ == '__main__':
    	app.run(debug=True,port=8000)
    	
