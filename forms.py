from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, TextField
from wtforms.validators import InputRequired, Length, Email, DataRequired


class ContactsForm(FlaskForm):
    name= TextField('Name' ,validators=[DataRequired()])
    email = TextField('Email',validators=[DataRequired()])
    phone = TextField('Phone',validators=[DataRequired()])
    message = TextAreaField('Your Message',validators=[DataRequired()])
    submit = SubmitField('Send')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Um username é obrigatório!'), Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    password = StringField('password', validators=[InputRequired('Uma password é obrigatória'),Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    confirmpassword = StringField('password', validators=[InputRequired('Passwords diferentes!'),Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    email = StringField('password', validators=[InputRequired('Uma password é obrigatória'),Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    remember = BooleanField('remember me')