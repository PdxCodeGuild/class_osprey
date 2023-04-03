from flask import Flask, render_template

app = Flask(__name__)

menu = ['ABOUT ME', 'ARCHIVE', 'CONTACTS']

posts = [
    {
        'title': 'Huge Update',
        'author': 'Firstname Lastname',
        'date': '3/28/23',
        'body': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vel turpis nunc eget lorem dolor. Faucibus interdum posuere lorem ipsum dolor sit amet. Lobortis mattis aliquam faucibus purus in massa tempor nec feugiat. At auctor urna nunc id cursus metus aliquam eleifend mi. Morbi blandit cursus risus at ultrices mi tempus imperdiet. Vitae turpis massa sed elementum tempus egestas sed sed risus. Velit scelerisque in dictum non. Nec nam aliquam sem et tortor. Gravida in fermentum et sollicitudin ac orci phasellus egestas tellus. Sit amet aliquam id diam maecenas ultricies mi eget. Aenean euismod elementum nisi quis. Sed libero enim sed faucibus turpis in eu. Arcu odio ut sem nulla pharetra diam sit amet. Neque egestas congue quisque egestas diam in arcu. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus. Nam aliquam sem et tortor. Ut porttitor leo a diam sollicitudin tempor. Luctus accumsan tortor posuere ac ut consequat.

Viverra aliquet eget sit amet tellus cras adipiscing. Ullamcorper a lacus vestibulum sed arcu. Viverra justo nec ultrices dui sapien eget mi. Lectus mauris ultrices eros in cursus. Quis enim lobortis scelerisque fermentum. Dui accumsan sit amet nulla facilisi morbi. Semper viverra nam libero justo laoreet. Quis risus sed vulputate odio ut enim blandit. Nunc id cursus metus aliquam eleifend mi in nulla. Sapien et ligula ullamcorper malesuada proin. Mattis rhoncus urna neque viverra justo nec ultrices dui.''',
    }, {
        'title': 'Some Title',
        'author': 'Firstname Lastname',
        'date': '3/26/23',
        'body': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vel turpis nunc eget lorem dolor. Faucibus interdum posuere lorem ipsum dolor sit amet. Lobortis mattis aliquam faucibus purus in massa tempor nec feugiat. At auctor urna nunc id cursus metus aliquam eleifend mi. Morbi blandit cursus risus at ultrices mi tempus imperdiet. Vitae turpis massa sed elementum tempus egestas sed sed risus. Velit scelerisque in dictum non. Nec nam aliquam sem et tortor. Gravida in fermentum et sollicitudin ac orci phasellus egestas tellus. Sit amet aliquam id diam maecenas ultricies mi eget. Aenean euismod elementum nisi quis. Sed libero enim sed faucibus turpis in eu. Arcu odio ut sem nulla pharetra diam sit amet. Neque egestas congue quisque egestas diam in arcu. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus. Nam aliquam sem et tortor. Ut porttitor leo a diam sollicitudin tempor. Luctus accumsan tortor posuere ac ut consequat.

Viverra aliquet eget sit amet tellus cras adipiscing. Ullamcorper a lacus vestibulum sed arcu. Viverra justo nec ultrices dui sapien eget mi. Lectus mauris ultrices eros in cursus. Quis enim lobortis scelerisque fermentum. Dui accumsan sit amet nulla facilisi morbi. Semper viverra nam libero justo laoreet. Quis risus sed vulputate odio ut enim blandit. Nunc id cursus metus aliquam eleifend mi in nulla. Sapien et ligula ullamcorper malesuada proin. Mattis rhoncus urna neque viverra justo nec ultrices dui.''',
    }, {
        'title': 'New Hobbies',
        'author': 'Firstname Lastname',
        'date': '3/15/23',
        'body': '''Really looking forward to learning Latin. Will keep you all updated.
        
Feel like I should have a little extra to read here.''',
    }
    ]

@app.route('/')
def blog_post():
    return render_template('index.html', posts=posts, menu=menu)

app.run(debug=True)
