from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
#inheriting from the base Form class. Then we created each field that we want to see in the contact form. 
#Instead of writing <input type="text">Name</input> in an HTML file, you write name = TextField("Name").
class ContactForm(Form):
  name = TextField("Name",  [validators.Required()])
  email = TextField("Email",  [validators.Required(), validators.Email()])
  subject = TextField("Subject",  [validators.Required()])
  message = TextAreaField("Message",  [validators.Required()])
  submit = SubmitField("Send")