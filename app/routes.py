import os
import secrets
from werkzeug.urls import url_parse
from app import app, db, models, bcrypt, Config
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from app.models import *
from sqlalchemy import text, func
from app.forms import LoginForm, RegistrationForm, ResetPasswordForm, RequestResetForm
from app.token import generate_confirmation_token, confirm_token
import datetime
import requests
from app.email import send_email, send_reset_email
from app.decorators import check_confirmed


############################################################################################################################################################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    
    recent_games = Games.query.order_by(Games.game_date.desc()).limit(4).all()
    featured_games = Games.query.order_by(Games.id_game.desc()).limit(4).all()
    #carousel_games = Games.query.order_by(Games.id_game.desc()).limit(3).all()
 
    return render_template('index.html', recent=recent_games, featured=featured_games) #carousel=carousel_games)



'''
@app.route('/newsletter', methods["GET", "POST"])
def subscribe_user(email,user_group_email, api_key):
    resp = requests.post(f"https://api.mailgun.net/v3/lists/{user_group_email}/members", 
            auth=("api", api_key),
            data=("subscribed": True,
                "email": email
    )
    return resp

'''
@app.route('/search<input>', methods=['GET', 'POST'])
def search(input):
    if request.method == 'POST':
        info = Games.query.get_or_404(id_game)
        keywords = request.form.get('search')
        unique_result = Games.query.filter(func.lower(Games.game_name) == func.lower(keywords)).first()
        if unique_result:
            #insert return redirect() to specific page using unique_result here
            results = Games.query.whooshee_search('teste').all()
    return render_template('products.html', results=results)

@app.route('/pesquisa/')
def pesquisa():
    error = None
    
    query = request.args.get('search')
    if len(query) < 3:
        error = 'Insira mais 3 ou mais letras para efetuar a pesquisa!'
        return redirect(url_for(request.endpoint))
    else:
        results = Games.query.whooshee_search(query).all()
        return render_template('products.html',  results=results)
    
  
   
    

@app.route("/tabelas")
@login_required
@check_confirmed
def tabelas():
    all_games = Games.query.all()
    all_genres = Genres.query.all()
    all_subplatforms = SubPlatforms.query.all()
    
    return render_template("tables.html", games = all_games, genres=all_genres, subplatforms=all_subplatforms) 

############################################################################################################################################################################################################
@app.route("/ordenargenero")
def ordenargenero():
   
    newest = Games.objects.filter(name__icontains=query).order_by(game_date)
    return render_template("products.html", newest=newest, oldest=oldest)

@app.route("/produtos/playstation")
def produtos_ps():
    
    results = db.engine.execute("SELECT * FROM games G INNER JOIN game_subplatform GS ON G.id_game = GS.id_games INNER JOIN subplatforms SP ON GS.id_subplat = SP.id_subplat INNER JOIN platforms P ON SP.id_plat = P.id_plat WHERE P.id_plat = 1 GROUP BY game_name")
  
    return render_template("products.html", results=results)

@app.route("/produtos/xbox")
def produtos_xbox():
   
    results = db.engine.execute("SELECT * FROM games G INNER JOIN game_subplatform GS ON G.id_game = GS.id_games INNER JOIN subplatforms SP ON GS.id_subplat = SP.id_subplat INNER JOIN platforms P ON SP.id_plat = P.id_plat WHERE P.id_plat = 2 GROUP BY game_name")
  
    return render_template("products.html", results=results)

@app.route("/produtos/nintendo")
def produtos_nintendo():
    
    results = db.engine.execute("SELECT * FROM games G INNER JOIN game_subplatform GS ON G.id_game = GS.id_games INNER JOIN subplatforms SP ON GS.id_subplat = SP.id_subplat INNER JOIN platforms P ON SP.id_plat = P.id_plat WHERE P.id_plat = 3 GROUP BY game_name")
       
    return render_template("products.html", results=results)

@app.route("/produtos/pc")
def produtos_pc():
   

    results = db.engine.execute("SELECT * FROM games G INNER JOIN game_subplatform GS ON G.id_game = GS.id_games INNER JOIN subplatforms SP ON GS.id_subplat = SP.id_subplat INNER JOIN platforms P ON SP.id_plat = P.id_plat WHERE P.id_plat = 4 GROUP BY game_name")
          
    return render_template("products.html", results=results)

@app.route("/produtos/show_all_recent")
def produtos_recent():
  
    results = db.engine.execute("SELECT * FROM games WHERE id_game ORDER BY game_date DESC ")
          
    return render_template("products.html", results=results)

@app.route("/produtos/show_all_featured")
def produtos_featured():
    page = request.args.get('page', 1, type=int)
    #query = db.engine.execute("SELECT * FROM games WHERE id_game ORDER BY id_game LIMIT 10")   
    #results = query.paginate(page=page, per_page=5)     
    results = Games.query.order_by(Games.id_game.desc()).paginate(page=page, per_page=5) 
    return render_template("products.html", results=results)

################################################################################################################################################################################################################################################   



################################################################################################################################################################################################################################################   

@app.route("/listajogos")
@login_required
@check_confirmed
def listajogos():
    return render_template("gameslist.html")

@app.route('/game/<id_game>', methods=["GET", "POST"])
def game(id_game):
    info = Games.query.get_or_404(id_game)
    similar=Games.query.order_by(Games.id_game.desc()).limit(4).all()
    return render_template("game.html", info=info, similar=similar)

###########################################################################################

@app.route('/editar', methods = ['GET', 'POST'])
def editar():
    if request.method == 'POST':
        game = Games.query.get(request.form.get('id'))
 
 
        game.game_name = request.form['name']
        game.game_image = request.form['image']
        game.game_preview1 = request.form['preview1']
        game.game_preview2 = request.form['preview2']
        game.game_preview3 = request.form['preview3']
        game.game_description = request.form['description']
        game.game_rating = request.form['rating']
        game.game_date = request.form['date']
        game.game_video = request.form['video']
        game.game_review = request.form['review']
        db.session.commit()

        flash("Jogo editado com sucesso", 'success')
 
        return redirect(url_for('tabelas'))
  
  


@app.route('/adicionarjogo', methods = ['GET', 'POST'])
def adicionar():
 
    if request.method == 'POST':
       
        selected_genres = request.form.getlist("genres")
        selected_subplatforms = request.form.getlist("subplatforms")
        flash(selected_genres)
        flash(selected_subplatforms)
       
        game_name = request.form['name']
        game_image = request.form['image']
        game_preview1 = request.form['preview1']
        game_preview2 = request.form['preview2']
        game_preview3 = request.form['preview3']
        game_description = request.form['description']
        game_rating = request.form['rating']
        game_date = request.form['date']
        game_video = request.form['video']
        game_review = request.form['review']
       

        game = Games(game_name,game_image, game_preview1, game_preview2, game_preview3, game_description, game_rating, game_date, game_video, game_review)
        

        db.session.add(game)
        db.session.commit()
 
        flash("Game Inserted Successfully", 'success')
            
        for value in selected_genres:
                statement = game_genre.insert().values(id_games=game.id_game, id_gen=value)
                db.session.execute(statement)
                db.session.commit()
                          
        for value in selected_subplatforms:
                statement = game_subplatform.insert().values(id_games= game.id_game, id_subplat=value)
                db.session.execute(statement)
                db.session.commit()
           
           
        return redirect(url_for('tabelas'))               

  
         
@app.route('/deletar/<id_game>/', methods = ['GET', 'POST'])
def deletar(id_game):
    game = Games.query.get(id_game)
    db.session.delete(game)
    db.session.commit()
    flash("Jogo deletado com sucesso", 'success')

    return redirect(url_for('tabelas'))

###########################################################################################

@app.route("/registo", methods=['GET', 'POST'])
def registo():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password, confirmed=False)
        db.session.add(user)
        db.session.commit()

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirmar_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Por favor, confirme o seu email."
        send_email(user.email, subject, html)
        login_user(user)

        flash('Um email de confirmação foi enviado por via email.', 'info')
        return redirect(url_for('unconfirmed'))
    return render_template('user/register.html', title='Registo', form=form)

@app.route('/confirmar/<token>')
@login_required
def confirmar_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('O Link the confirmação é invalido ou expirou.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Conta já confirmada. Por favor execute o login', 'info')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('A sua conta foi confirmada. Obrigado!', 'success')
    return redirect(url_for('index'))



@app.route('/não_confirmado')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect('index')
    flash('Por favor, confirme a sua conta', 'warning')
    return render_template('user/unconfirmed.html')

@app.route('/reenviar')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('confirmar_email', token=token, _external=True)
    html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = "Por favor confirme o seu email!"
    send_email(current_user.email, subject, html)
    flash('Um novo email com um link de confirmação foi enviado', 'info')
    return redirect(url_for('unconfirmed'))

@app.route('/reenviar_password')
@login_required
def resend_confirmation_password():
    
    send_reset_email(user)
    flash('Um novo email com um link de confirmação foi enviado', 'info')
    return redirect(url_for('reset'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            # remember_me=form.remember_me.data
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login sem sucesso. Por favor verifique o seu email e password', 'danger')
    return render_template('user/login.html', title='Login', form=form)


def send_password_reset_email(email):
    password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
 
    password_reset_url = url_for(
        'user/reset_with_token',
        token = password_reset_serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT']),
        _external=True)
 
    html = render_template(
        'user/reset_password.html',
        password_reset_url=password_reset_url)
 
    send_email('Solicitação de reposição de password.', [email], html)

   

@app.route("/reset_password", methods=['GET', 'POST'])
def reset():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  
        send_reset_email(user) 
        #token = generate_confirmation_token(user)
        #confirm_url = url_for('reset_with_token', token=token, _external=True)
        #html = render_template('user/email_password_reset.html', confirm_url=confirm_url)
        #subject = "Solicitação de reposição de password"
        
        send_email(user, subject, html)
        flash('Um email foi enviado com instruções para repor a sua password.', 'info')
        return redirect(url_for('login'))
    return render_template('user/reset_password.html', title='Repor Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_with_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('O Link the confirmação é invalido ou expirou.', 'warning')
        return redirect(url_for('reset'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password_hash = hashed_password
        db.session.commit()
        flash('A sua password foi atualizada! Pode agora logar na sua conta.', 'success')
        return redirect(url_for('login'))
    return render_template('user/reset_password_with_token.html', title='Repor Password', form=form)


 
@app.route('/logout')
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('index'))

###########################################################################################
