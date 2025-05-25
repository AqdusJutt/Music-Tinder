from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("lyrics.csv")

# Fill missing values
df.fillna("", inplace=True)

# TF-IDF Vectorizer on lyrics
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['lyrics'])

# Get top N popular songs (could also be by views/popularity if available)
popular_songs = df[['song_name', 'artist']].head(5).to_dict(orient='records')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/find-song', methods=['GET', 'POST'])
def find_song():
    result = None
    lyrics_input = ""
    if request.method == 'POST':
        lyrics_input = request.form['lyrics_snippet']
        input_vec = vectorizer.transform([lyrics_input])
        similarity = cosine_similarity(input_vec, tfidf_matrix)
        index = similarity.argmax()
        result = df.iloc[index][['song_name', 'artist', 'genre']].to_dict()
    return render_template('find_song.html', query=lyrics_input, result=result, popular_songs=popular_songs)

@app.route('/find-lyrics', methods=['GET', 'POST'])
def find_lyrics():
    result = None
    song_input = ""
    if request.method == 'POST':
        song_input = request.form['song_name'].strip().lower()
        filtered = df[df['song_name'].str.lower() == song_input]
        if not filtered.empty:
            result = filtered.iloc[0].to_dict()
    return render_template('find_lyrics.html', query=song_input, result=result)

@app.route('/genres', methods=['GET', 'POST'])
def genre_explorer():
    genres = sorted(df['genre'].dropna().unique())
    selected_genre = request.form.get('genre') if request.method == 'POST' else None
    search_query = request.form.get('search') if request.method == 'POST' else ''
    
    filtered_genres = [g for g in genres if search_query.lower() in g.lower()] if search_query else genres

    songs = []
    if selected_genre:
        songs = df[df['genre'].str.lower() == selected_genre.lower()][['song_name', 'artist']].to_dict(orient='records')

    return render_template('genres.html', genres=filtered_genres, selected_genre=selected_genre, songs=songs, search_query=search_query)

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)
