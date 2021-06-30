from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///pokedex.db")

## each route is associated with a function
@app.route("/")
def pokedex():
    # TODO: return a list of dictionaries from our database containing the name and corresponding image of each pokemon in the fist row of our display
    first = db.execute('TODO')

    # TODO: return a list of dictionaries from our database containing the name and corresponding image of each pokemon in the middle row of our display
    middle = db.execute('TODO')

    # TODO: return a list of dictionaries from our database containing the name and corresponding image of each pokemon in the last row of our display
    last = db.execute('TODO')

    return render_template("pokemon.html", first = first, middle = middle, last = last)

@app.route("/display", methods=["GET", "POST"])
def disp():
    if request.method == "POST":
        name = request.form.get("pokemon")

        # TODO: return a list of dictionaries from our database containing the image and corresponding background color of the pokemon returned from the form
        selected = db.execute('TODO')

        # pass the 0th (and only) index of the selected list of dictionaries to the template for closeup display
        return render_template("display.html", selected = selected[0])
    else:
        return redirect("/")
