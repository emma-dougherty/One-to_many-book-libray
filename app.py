from flask import Flask, render_template
from controllers.book_controller import books, books_blueprint
app = Flask(__name__)
app.register_blueprint(books_blueprint)