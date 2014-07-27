#to active the enviroment just type . bin/activate

#First. we imported the Flask class and a function render_template.
from flask import Flask, render_template, request, flash
#Importing forms, preventing a CSRF attack
from forms import ContactForm

from flask.ext.mail import Message, Mail
 
#we created a new instance of the Flask class.
app = Flask(__name__)  

#To prevent CSFR
#One way to do this is to keep a unique token hidden inside your HTML <form> tag that cannot be guessed by attackers. 
#When the form POSTs to your server, the token is checked first. 
#If the token does not match, your server rejects the form submission and does not touch the form data. 
#If the token matches, the server proceeds with form handling and validation.
app.secret_key = 'yo me llamo Ralf' #conviene que sea algo mas compleja ;) 
 
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'moises.full.ios@gmail.com'
app.config["MAIL_PASSWORD"] = 'nirvana4488'
 
mail.init_app(app)
 
  
 
#We then mapped the URL / to the function home(). Now, when someone visits this URL, the function home() will execute. 
@app.route('/')
def home():#The function home() uses the Flask function render_template() to render the home.html template we just created from the templates/ folder to the browser.
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/test')
def test():
  return render_template('test.html')

@app.route('/test/espaniol')
def testEspaniol():
  return render_template('espaniol/test_espaniol.html') 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='moises.full.ios@gmail.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

#Finally, we use run() to run our app on a local server. 
#We'll set the debug flag to true, so we can view any applicable error messages if something goes wrong, 
#and so that the local server automatically reloads after we've made changes to the code. 
if __name__ == '__main__':
  app.run(debug=True)