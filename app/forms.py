
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, TextField, IntegerField,  DateField, SelectField
from wtforms.validators import InputRequired, Length, Email, DataRequired, EqualTo, ValidationError, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User, Games



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message='Insira um email'), Email(message='Email inválido')])
    password = PasswordField('Password', validators=[InputRequired(message='Insira uma password')])
    remember_me = BooleanField('Lembre-me')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(), Length(min=7, max=20, message='Deve ser entre 7 a 20 letras')]) # Validators to provide a basic requirement for the username
    email = StringField('Email', validators=[InputRequired(message='Insira um email'), Email(message='Email inválido')])
    password = PasswordField('Password', validators=[InputRequired(message='Insira uma password')])
    confirm_password = PasswordField('Confirme Password', validators=[InputRequired(message='é necessário confirmar a password'), EqualTo('password')])
    submit = SubmitField('Inscreva-se')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Nome de Utilizador já existente!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email já existente!')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Solicitar reposição de password')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Não existe nenhuma conta com esse email. Deve se registar primeiro')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Repor Password')