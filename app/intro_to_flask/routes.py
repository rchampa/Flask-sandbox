#to active the enviroment just type . bin/activate
from intro_to_flask import app
#First. we imported the Flask class and a function render_template.
from flask import render_template, request, flash, session, url_for, redirect
#Importing forms, preventing a CSRF attack
from forms import ContactForm, SignupForm, SigninForm

from flask.ext.mail import Message, Mail 
mail = Mail() 
  
 
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
      msg = Message(form.subject.data, sender='ricardo@myapp.com', recipients=['moises.full.ios@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)


from models import db, User

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:   
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      #Saving session variable 
      session['email'] = newuser.email

      #return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)


@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))

from models import db
'''@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
'''
#Finally, we use run() to run our app on a local server. 
#We'll set the debug flag to true, so we can view any applicable error messages if something goes wrong, 
#and so that the local server automatically reloads after we've made changes to the code. 
if __name__ == '__main__':
  app.run(debug=True)