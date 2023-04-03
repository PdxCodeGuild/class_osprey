# Lab03 Blog, Flask set up 
from flask import Flask, render_template, request



app = Flask(__name__)

# test, cant have this and page content at the same route
# @app.route('/')
# def hello_world():
#     return("hello world!")


POSTS= [
    {
        'title': "Cabot Cove, Maine",
        'author': "Blogger McBlogface",
        'date': "September 1st, 2022",
        'body': "Aftertaste doppio, iced acerbic sugar cappuccino, bar  cortado single shot shop turkish. So bar  coffee organic, cortado latte java wings roast black. Blue mountain crema milk cinnamon, variety caramelization latte robust grinder. Cappuccino cream decaffeinated robusta, acerbic single shot white, crema acerbic flavour instant organic."
    }, 
        {
        'title': "Yosemite National Park",
        'author': "Blogger McBlogface",
        'date': "October 1st, 2022",
        'body': "Meow meow pee in shoe leave fur on owners clothes always ensure to lay down in such a manner that tail can lightly brush human's nose . Stare at wall turn and meow stare at wall some more meow again continue staring catching very fast laser pointer get suspicious of own shadow then go play with toilette paper, and poop on couch, or spit up on light gray carpet instead of adjacent linoleum. Stare at guinea pigs use lap as chair, so scamper."
    }, 
       {
        'title': "Bodega Bay",
        'author': "Blogger McBlogface",
        'date': "November 1st, 2022",
        'body': "The last time you had a cheeseburger was too long ago. Try not to drool when you think about the slightly charred, medium-rare meat nestled between soft brioche, cradled in crisp iceberg lettuce and flavour amplifying condiments. Why are you still reading this- go get a cheeseburger."
    }, 
        {
        'title': "Boreal Skiing",
        'author': "Blogger McBlogface",
        'date': "December 1st, 2022",
        'body': "Lemon drops muffin dessert cookie macaroon cheesecake dessert. Macaroon marshmallow fruitcake brownie candy bonbon. Apple pie jelly-o sesame snaps wafer marshmallow shortbread tart. Bonbon carrot cake sweet roll marzipan carrot cake gingerbread croissant gummi bears. Candy macaroon wafer halvah sesame snaps gummi bears chocolate."
    }, 
]

@app.route('/')
def page_content():
    content = {
        "post": POSTS
    }
    return render_template('index.html', content=content)


app.run(debug=True)