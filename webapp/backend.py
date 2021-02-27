#to activate virtual environment
#venv\Scripts\activate
#to import images
#https://stackabuse.com/serving-static-files-with-flask/
#https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
#upgrading pip
#https://stackoverflow.com/questions/15221473/how-do-i-update-pip-itself-from-inside-my-virtual-environment
#deactivate  - to stop virtual environment


from flask import Flask, render_template
from statsBot import totdata,statedata
from newsBot import newsScraper

my_app = Flask(__name__)

#importing state data by scraping
state = totdata()

#importing news data by scraping
links,linksTexts = newsScraper('https://economictimes.indiatimes.com/news/coronavirus',['Coronavirus','pandemic','COVID-19','vaccine','India'])

@app.route("/")
@app.route("/index.html")
@app.route("/home")
def home():
    return render_template("index.html",news  =  linksTexts)

@app.route("/aboutus")
@app.route("/aboutus.html")
def aboutus():
    return render_template("aboutus.html")


@app.route("/table.html")
@app.route("/table")
def table():
    return render_template("table.html",states  =  state)


if __name__ == "__main__":
    my_app.run(debug=True)
