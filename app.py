from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    genres = {
        'Science Fiction': ['Dune by Frank Herbert', 'Neuromancer by William Gibson', 'Foundation by Isaac Asimov'],
        'Mystery': ['The Girl with the Dragon Tattoo by Stieg Larsson', 'Gone Girl by Gillian Flynn', 'The Da Vinci Code by Dan Brown'],
        'Fantasy': ['The Lord of the Rings by J.R.R. Tolkien', 'Harry Potter and the Sorcerer\'s Stone by J.K. Rowling', 'A Game of Thrones by George R.R. Martin'],
        'Thriller': ['The Silence of the Lambs by Thomas Harris', 'The Bourne Identity by Robert Ludlum', 'The Firm by John Grisham'],
        'Romance': ['Pride and Prejudice by Jane Austen', 'Outlander by Diana Gabaldon', 'Me Before You by Jojo Moyes']
    }
    return render_template('index.html', genres=genres)

if __name__ == '__main__':
    app.run(debug=True)
