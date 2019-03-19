from flask import Flask,url_for,request,redirect,send_from_directory,render_template
from werkzeug.utils import secure_filename
import os	
from os import listdir
import pickle,pandas as pd
from abc_new import mpq


UPLOAD_FOLDER = './upload'

app =Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
@app.route('/')
def abc():	
	return render_template('abcd.html')


@app.route('/kaam',methods ={'GET','POST'})
def kaam():
	if request.method =='POST':
		uploaded_file =request.files.getlist('file[]')
		foldername=request.form['foldername']
		filenames=[]
		folder_path=dir_path+'/upload/'+foldername
		os.mkdir(folder_path)
		for file in uploaded_file:
			
			filename = secure_filename(file.filename)
			file.save(os.path.join('./upload/%s'%foldername, filename))	
			filenames.append(filename)
		return render_template('abcd1.html',message=filenames,message2=foldername)
		 
		
	else :
		file =request.args.get('file[]')
		return "done"
		
@app.route('/upload/<name>')
def upload(name):
	return send_from_directory(app.config['./upload'],name)
	

@app.route('/execute',methods={'GET','POST'})
def cdb():
	#load saved model
	loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
	
	foldername=request.form['foldername']
	folder_path=dir_path+'/upload/'+foldername
	filenames=listdir(folder_path)
	filenames.sort()
	x1=[]
	with open('output.txt', 'w') as outfile:
		for fname in filenames:
			with open(folder_path+"/"+fname) as infile:
				li1 =mpq(folder_path+"/"+fname)
				x = pd.DataFrame([li1])
				result = loaded_model.predict(x)
				x1.append(result[0])
				for line in infile:
					outfile.write(line)
	
	
	
	from statistics import mean 
	z= mean(x1)
	
	
	li =mpq("output.txt")
	
	data = pd.read_csv("kc1.csv")
	x = pd.DataFrame([li])
	result = loaded_model.predict(x)
	if(result[0]>=0.5):
		ans="Yes with value= "+str(result[0])
	else:
		ans="No with value= "+str(result[0])
	if(z>=0.5):
		ans1="Yes with value= "+str(round(z,2))
	else:
		ans1="No with value= "+str(round(z,2))
	y=str(result[0])+" "+str(round(z,2))
	
	return render_template('final.html',message=ans,message2=ans1)

if __name__=='__main__':
	app.run()	