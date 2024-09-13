import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    # Load the books and ratings datasets
    books = pd.read_csv('data/BX-Books.csv', delimiter=';', encoding='latin-1', error_bad_lines=False)
    ratings = pd.read_csv('data/BX-Book-Ratings.csv', delimiter=';', encoding='latin-1', error_bad_lines=False)
    return books, ratings

def recommend_books(book_title, books):
    # Vectorize the book titles
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(books['Book-Title'].fillna(''))

    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get index of the book
    try:
        idx = books.index[books['Book-Title'] == book_title].tolist()[0]
    except IndexError:
        return []

    # Get similarity scores for all books
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top 5 books
    book_indices = [i[0] for i in sim_scores[1:6]]

    return books['Book-Title'].iloc[book_indices].tolist()
