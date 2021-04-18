# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:25:58 2021

@author: DEBJYOTI
"""
import os
import numpy
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
from keras.models import load_model

model = load_model('trafficSignModel.h5')


classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }



app = Flask(__name__)

upload_folder = os.path.join('static', 'Test')
app.config['UPLOAD'] = upload_folder


@app.route('/')
def index():
   return render_template('traffic.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

   image = Image.open(f)
   img_path = os.path.join(app.config['UPLOAD'], f.filename)
   image = image.resize((30,30))
   image = numpy.expand_dims(image, axis=0)
   image = numpy.array(image)
   pred = model.predict_classes([image])[0]
   sign = classes[pred+1]	
   
   return render_template('traffic.html',selected_img=img_path,
   sign_pred=sign)
  
    
  
if __name__ == '__main__':
   app.run(debug = True, port=4000)