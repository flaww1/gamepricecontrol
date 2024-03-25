from flask_mail import Message
from flask import url_for
from app import app, mail


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)
'''
def send_reset_email(user, subject, template):
    token = user.get_reset_token()
    msg = Message(subject,
        html=template,
        recipients=[user.email],
        sender=app.config['MAIL_DEFAULT_SENDER']
    )         
    mail.send(msg)
    '''
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Solicitação de Reposição de Password',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''Para repor a password, siga o seguinte link:
{url_for('reset_with_token', token=token, _external=True)}
Se não fez este pedido, ignore este email.
'''
    mail.send(msg)