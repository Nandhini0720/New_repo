

from turtle import title
from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
    'author' : 'Nandhini',
    'title' : 'blog-post 1',
    'content' : 'blog post content 1',
    'date_posted' : '12th October, 2022'
    },

    {
    'author' : 'Kalidass',
    'title' : 'blog-post 2',
    'content' : 'blog post content 2',
    'date_posted' : '15th October, 2022'
    }
    ]


@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
    app.run(debug=True)