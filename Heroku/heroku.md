# heroku-flask-deployment-guide
Guide to deploy in heroku using flask.
alternatively use this [link](https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524) for detailed guide.

- Install flask and gunicorn
```
pip install flask gunicorn
```

- Upgrade pip to the latest version
```
pip install --upgrade pip
```

- Python dependencies installed
```
pip freeze
```

- Python dependencies installed details added to requirements.txt
save this file in the directory needed heroku will install necessary dependencies through this , remove uneccessary ones
```
pip freeze > requirements.txt
```

- Add Procfile, Procfile can be viewed via this [link](https://github.com/lonlander/heroku-flask-deployment-guide/blob/master/Procfile).

- gunicorn lets us use html files in parallel(need to be updated)

### after that follow this ,though this is provided in heroku itself

- Install the Heroku CLI,Download and install the Heroku CLI.
- If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
heroku login 
```
- Create a new Git repository
- Initialize a git repository in a new or existing directory

``` 
cd my-project/
git init
heroku git:remote -a covid-tracker101
```
- Deploy your application
- Commit your code to the repository and deploy it to Heroku using Git.
```
git add .`
git commit -am "make it better"
git push heroku master
```
- You can now change your main deploy branch from "master" to "main" for both manual and automatic deploys, please follow the instructions here.
### Existing Git repository
- For existing repositories, simply add the heroku remote

```
heroku git:remote -a covid-tracker101
```


