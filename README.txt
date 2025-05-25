🎵 MUSIC TINDER – MUSIC RETRIEVAL SYSTEM
----------------------------------------

📌 PROJECT OVERVIEW:
Music Tinder is a web-based tool where users can:
1. 🎤 Find songs using just lyrics.
2. 📝 Find lyrics by entering a song name.
3. 🎧 Explore songs by genre.
4. 📊 View visual insights like genre stats and word clouds.
5. 👥 See information about the project team.

This is part of our "Information Retrieval" (IR) course at Air University.
We applied concepts like:
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Lyrics classification using Machine Learning
- Search relevance & retrieval


📂 PAGES INCLUDED IN THE PROJECT:
---------------------------------
1. Home Page – With buttons to navigate all features.
2. Find Songs – Enter part of lyrics → Get matching song & genre.
3. Find Lyrics – Enter song name → Get full lyrics.
4. Genre Explorer – View a list of songs by genre.
5. Song Insights – Charts showing genre counts and word clouds.
6. Team – Information about us (project creators).


🧠 HOW IT WORKS (SIMPLE VERSION):
----------------------------------
- When the user types lyrics, we calculate similarity using TF-IDF and show the closest song.
- When user types a song name, we search and show the lyrics.
- For genre prediction, we use a machine learning classifier trained on the lyrics.
- Everything works in real-time using Python + Flask.


✅ REQUIREMENTS:
----------------
To run this project, make sure you have:
- Python 3 installed
- Required libraries installed:
    flask, pandas, scikit-learn, matplotlib, wordcloud

To install libraries:
Type the following in the terminal/command prompt:
    pip install flask pandas scikit-learn matplotlib wordcloud


🚀 HOW TO RUN:
--------------
1. Make sure all files (HTML, app.py, dataset, music.png) are in one folder.
2. Open terminal or command prompt in that folder.
3. Run the Python file:
    python app.py
4. Now open your browser and go to:
    http://127.0.0.1:5000

You will see the homepage with buttons to explore songs, lyrics, genres, and visual stats.


🎓 NOTE FOR TEACHER:
---------------------
- This project uses real Spotify music data to search and display music information.
- We tried to keep everything simple, colorful, and easy to use.
- It’s fully working with lyrics-based search, genre classification, and visualization.
- We applied key IR concepts like term frequency, inverse document frequency, and basic machine learning.


👨‍💻 DEVELOPED BY:
-------------------
Team from Air University  
Semester: Spring 2025  
Subject: Information Retrieval (IR)


Thank you for checking out our project! 😊
