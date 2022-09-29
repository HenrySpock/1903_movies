from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension 

app = Flask(__name__)
app.config['SECRET_KEY'] = "ml_sec"

debug = DebugToolbarExtension(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# MOVIES = ['Amadeus', 'Chicken Run', 'Dances With Wolves']
MOVIES = {'Amadeus', 'Chicken Run', 'Dances With Wolves'}
# MOVIES was a list, but now it's a set for demonstrion of flash messaging.

@app.route("/")
def home_page():
    """Shows home page"""
    return render_template('home.html')

@app.route("/movies")
def show_all_movies():
    """Show list of all movies in fakedb."""
    return render_template("movies.html", movies=MOVIES)
#notice here that movies is set to a globally scoped variable MOVIES    

@app.route("/movies/new", methods=["POST"])
def add_movie():
    title = request.form['title']
    # Add to pretend DB 
    # MOVIES.append(title)
    if title in MOVIES:
        flash('Movie Already Exists!', 'error')
    else:
        MOVIES.add(title)
        #.append() changed to .add() because MOVIES changed from list to set
        # return render_template('movies.html', movies=MOVIES) : causes POST issue with resubmission
        flash('Created your Movie!', 'success')
    return redirect('/movies')
    #This redirect gets us off of the "POST" route where resubmissions can occur.

@app.route('/oldhp')
def redirect_to_home():
    """Redirects user to new home page."""
    flash('That page has moved! This is our new home page! I only show up the first time!')
    return redirect("/movies")