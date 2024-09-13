from flask import Flask, request, jsonify
from recommendation import load_data, recommend_books

app = Flask(__name__)

# Load data
books, ratings = load_data()

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get the book title from the query string
    book_title = request.args.get('book_title')
    
    # Get book recommendations
    recommendations = recommend_books(book_title, books)
    
    # Return the recommendations as a JSON response
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
