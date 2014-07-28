from flask import Flask

#we created a new instance of the Flask class.
app = Flask(__name__)  

#To prevent CSFR
#One way to do this is to keep a unique token hidden inside your HTML <form> tag that cannot be guessed by attackers. 
#When the form POSTs to your server, the token is checked first. 
#If the token does not match, your server rejects the form submission and does not touch the form data. 
#If the token matches, the server proceeds with form handling and validation.
app.secret_key = 'yo me llamo Ralf' #conviene que sea algo mas compleja ;)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'moises.full.ios@gmail.com'
app.config["MAIL_PASSWORD"] = 'nirvana4488'
 
from routes import mail
mail.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/myflaskdb'
 
from models import db
db.init_app(app)