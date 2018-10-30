from flask import Flask ,render_template, redirect, url_for, session, request, logging
import requests

app = Flask(__name__)
@app.route('/', methods=['GET','POST']) #landing page
def home():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "u2h238hr2938hr":
            return redirect(url_for('level2'))
    return render_template("1.html")

@app.route('/iwoediwdowiejdw', methods=['GET','POST']) #landing page
def level2():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "o2j3p23j0f-kodomfewf":
            return redirect(url_for('level3'))
    return render_template("2.html")

@app.route('/password', methods=['GET','POST']) #landing page
def password():
    return "o2j3p23j0f-kodomfewf"


@app.route('/iwoediwwofiweijfowi', methods=['GET','POST']) #landing page
def level3():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "rh8392rh832h2u":
            return redirect(url_for('level4'))
    return render_template("3.html")

@app.route('/wedwedoediwwofiweiowi', methods=['GET','POST']) #landing page
def level4():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "we_attack_when_the_moon_rises":
            return redirect(url_for('level5'))
    return render_template("4.html")

@app.route('/wedwedoediwwwewef23', methods=['GET','POST']) #landing page
def level5():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "why_so_serious":
            return redirect(url_for('level6'))
    return render_template("5.html")

@app.route('/hidden_image', methods=['GET','POST']) #landing page
def hidden_image():
    return render_template("hidden_image.html")

@app.route('/wedwedo232d4fwef23', methods=['GET','POST']) #landing page
def level6():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "hello_from_the_other_side":
            return redirect(url_for('level7'))
    return render_template("6.html")

@app.route('/hidden_audio', methods=['GET','POST']) #landing page
def hidden_audio():
    return render_template("hidden_audio.html")

@app.route('/wedwedo232d4kmo0l0oik', methods=['GET','POST']) #landing page
def level7():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        if password == "azure":
            return redirect(url_for('level8'))
    return render_template("7.html")

@app.route('/wedwedwefwefd4kmo0l0oik', methods=['GET','POST']) #landing page
def level8():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        password = password.lower()
        
        if password == "2f8efa417b53a39d4356340e6ea30722acd701ae39f1cbef19738a6897b321c2":
            return redirect(url_for('level9'))
    return render_template("8.html")

@app.route('/wedwedwefwefd4kmo0mlil0oik', methods=['GET','POST']) #landing page
def level9():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        
        
        if password == "buhahahahahahXD":
            return redirect(url_for('level10'))
    return render_template("9.html")

@app.route('/hidden_image_text', methods=['GET','POST']) #landing page
def hidden_image_text():
    return render_template("hidden_image_text.html")

@app.route('/7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069', methods=['GET','POST']) #landing page
def level10():
    if request.method=="POST":
        password = request.form['password']
        password = str(password)
        
        if password == "Hello World!":
            return redirect(url_for('finish'))
    return render_template("10.html")

@app.route('/7f83b1jfi26d9069', methods=['GET','POST']) #landing page
def finish():
   return render_template("finish.html")

if __name__=='__main__':

	app.run(debug=True,host="0.0.0.0",port=80)