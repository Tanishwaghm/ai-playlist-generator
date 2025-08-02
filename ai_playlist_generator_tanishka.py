
import streamlit as st
import random

# Set page config
st.set_page_config(page_title="AI Playlist Generator", page_icon="🎵", layout="centered", initial_sidebar_state="auto")

# Spotify logo and dark background
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .reportview-container {
        background: #121212;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🎧 AI-Based Playlist Generator")
st.markdown("### by **Tanishka Waghmare**")
st.image("https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Green.png", width=150)

mood = st.selectbox("🎭 Select Your Mood", ["Happy", "Sad", "Chill", "Energetic"])
activity = st.selectbox("🏃 Select Your Activity", ["Study", "Workout", "Travel", "Relax"])
city = st.text_input("🌦️ Enter Your City for Weather", placeholder="e.g., Pune")

# Simulate weather condition (mock)
weather = random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])

# Playlist logic
def generate_playlist(mood, activity, weather):
    all_songs = {
        "Happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"],
        "Sad": ["Someone Like You - Adele", "Let Her Go - Passenger"],
        "Chill": ["Sunflower - Post Malone", "Location - Khalid"],
        "Energetic": ["Stronger - Kanye West", "Eye of the Tiger - Survivor"],
        "Study": ["Weightless - Marconi Union", "Intro - The xx"],
        "Workout": ["Till I Collapse - Eminem", "POWER - Kanye West"],
        "Travel": ["Adventure of a Lifetime - Coldplay", "Home - Edward Sharpe"],
        "Relax": ["Breathe Me - Sia", "Skinny Love - Bon Iver"],
        "Rainy": ["Set Fire to the Rain - Adele", "Riptide - Vance Joy"],
        "Sunny": ["Walking on Sunshine - Katrina & The Waves", "Island in the Sun - Weezer"],
        "Cloudy": ["Demons - Imagine Dragons", "Sweater Weather - The Neighbourhood"],
        "Windy": ["Dust in the Wind - Kansas", "Blown Away - Carrie Underwood"]
    }
    songs = list(set(all_songs.get(mood, []) + all_songs.get(activity, []) + all_songs.get(weather, [])))
    random.shuffle(songs)
    return songs[:5]

if st.button("🎶 Generate Playlist"):
    if city:
        st.success(f"Weather in {city} is *{weather}* today.")
        playlist = generate_playlist(mood, activity, weather)
        st.subheader("🎵 Your Personalized Playlist:")
        for idx, song in enumerate(playlist, 1):
            st.markdown(f"{idx}. {song}")
    else:
        st.warning("Please enter your city for weather input.")
