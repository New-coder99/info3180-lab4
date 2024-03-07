from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])



class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])