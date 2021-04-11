from flask import Flask, render_template, request, url_for
# from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
app = Flask(__name__)
#run_with_ngrok(app)
#app.config['WqdGh8X0OI.mp4']
from predict import run
@app.route('/')
@app.route('/home',methods = ['GET', 'POST'])
def home():
 
  return render_template('website.html')


	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'Your file was uploaded successfully'

if __name__ == '__main__':
  app.run()