from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user and ask user if they'd like to play."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Ask user to fill in madlibs fields"""

    user_response = request.args.get("yesno")

    if user_response == 'no':
        return render_template("goodbye.html")

    colors = ['blue', 'pink', 'green', 'yellow']
    adjectives = ['super', 'neat', 'tired', 'happy', 'shiny']
    return render_template("game.html",
                           colors=colors,
                           adjectives=adjectives)


@app.route('/madlib', methods=['POST', 'GET'])
def show_madlib():
    """Show filled in madlibs to user"""

    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.getlist("adj")

    return render_template("madlib.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
