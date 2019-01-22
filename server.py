"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = ['dummkopf', 'rumpelstilzchen', 'babadook', 'boogey man', 'silly sausage']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        Hi! This is the home page. 
        <a href="/hello">Go to Hello!</a>
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    option_string = ""
    for item in AWESOMENESS:
      print(item)

      # print("""
      # <option value ="{}">{}</option>
      # """.format(item, item))


      option_string += """
      <option value ="{}">{}</option>
      """.format(item, item)

      print('option string:', option_string)

    html_string = """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="awesomeness">
    """ + option_string + """
          </select> <br> <br>
          <input type="submit" value="Submit">
        </form>
        <a href="/diss">Go to disses!</a>
      </body>
    </html>
    """

    return html_string

    # return """
    # <!doctype html>
    # <html>
    #   <head>
    #     <title>Hi There!</title>
    #   </head>
    #   <body>
    #     <h1>Hi There!</h1>
    #     <form action="/greet">
    #       What's your name? <input type="text" name="person">
    #       <select name="awesomeness">
    #         <option value="awesome">Awesome</option>
    #         <option value="terrific">Terrific</option>
    #         <option value="fantastic">Fantastic</option>
    #         <option value="neato">Neato</option>
    #         <option value="fantabulous">fantabulous</option>
    #         <option value="wowza">Wowza</option>
    #         <option value="oh-so-not-meh">oh-so-not-meh</option>
    #         <option value="brilliant">Brilliant</option>
    #         <option value="ducky">Ducky</option>
    #         <option value="coolio">Coolio</option>
    #         <option value="incredible">Incredible</option>
    #         <option value="wonderful">Wonderful</option>
    #         <option value="smashing">Smashing</option>
    #         <option value="lovely">Lovely</option> 
    #       </select> <br> <br>
    #       <input type="submit" value="Submit">
    #     </form>
    #     <a href="/diss">Go to disses!</a>
    #   </body>
    # </html>
    # """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    # compliment = request.args.get("awesomeness")
    attribute = request.args.get("awesomeness")

    if attribute == None:
        attribute = request.args.get("disses")

    # compliment = choice(AWESOMENESS)

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, attribute)

@app.route("/diss")
def diss_person():

      return """
      <!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi There!</h1>
          <form action="/greet">
            What's your name? <input type="text" name="person">
            <select name="disses">
              <option value="dummkopf">Dummkopf</option>
              <option value="rumpelstilzchen">Rumpelstilzchen</option>
              <option value="rumpus">Rumpus</option>
              <option value="babadook">Babadook</option>
              <option value="boogey man">Boogey Man</option>
              <option value="silly sausage">Silly Sausage</option>
            </select> <br> <br>
            <input type="submit" value="Submit">
          </form>
          <a href="/diss">Go to disses!</a>
        </body>
      </html>
      """




if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
