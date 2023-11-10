from flask import render_template, flash, redirect, url_for, request
from app import app_inst, db
from app.forms import LoginForm, RegistrationForm, FilmFinder, FilmDetails
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from imdb import Cinemagoer

@app_inst.route('/')
@app_inst.route('/index')
@login_required
def index():
    title = 'Hauptseite'
    body = 'Rick, Berend, Joris, Jan'
    return render_template('index.html', title=title, body=body)


@app_inst.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


@app_inst.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app_inst.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app_inst.route('/film/<id>/<title>/<year>', methods=['GET'])
def openMovies(id,title,year):
    movie = Cinemagoer().get_movie(id)
    movieList = {}
    #movieList['imdbID'] = movie['imdbI']
    movieList['imdbID'] = id
    movieList['title'] = title
    movieList['year'] = year
    movieList['genres'] = movie['genres']
    movieList['runtime'] = movie['runtimes'][0]
    genre_amount = len(movie['genres'])
    if(genre_amount == 1):
        movieList['weight'] = "1"
    else:
        movieList['weight'] =f"1/{genre_amount}"
    movieList['rating'] = movie['rating']
    # print(movie.infoset2keys)
    return render_template('filmdetails.html', movie=movieList)

@app_inst.route('/filmfinder', methods=['GET', 'POST'])
def filmfinder():
    search_movie = FilmFinder()
    get_movie_details = FilmDetails()
    ia = Cinemagoer()   
    if search_movie.submit.data:
        search = search_movie.search.data
        search_result = ia.search_movie(search)
        return render_template('filmfinder.html', title='find movie', search_movie=search_movie, get_movie_details=get_movie_details, search=search_result)
    return render_template('filmfinder.html', title='find movie', search_movie=search_movie, get_movie_details=get_movie_details)
