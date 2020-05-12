
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, TextField
from wtforms.validators import InputRequired, Length, Email, DataRequired, EqualTo, ValidationError



class LoginForm(FlaskForm):
    uti_nome = StringField('username', validators=[InputRequired('Um username é obrigatório!'), Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    uti_password = StringField('password', validators=[InputRequired('Uma password é obrigatória'),Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])
    uti_email = StringField('password', validators=[InputRequired('Uma password é obrigatória'),Length(min=7, max=15, message='Deve ser entre 7 a 15 letras')])


class RegistrationForm(FlaskForm):
    uti_nome = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)]) # Validators to provide a basic requirement for the username
    uti_email = StringField('Email', validators=[DataRequired(), Email()])
    uti_password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Retype Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken! Please try another username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exists.')


