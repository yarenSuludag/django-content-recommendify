from django.shortcuts import render
import random
import requests
from django.http import JsonResponse

# API Anahtarları
TMDB_API_KEY = "19e720bc291a6010f4fc42ba47360ec0"
SPOTIFY_CLIENT_ID = "3fc3c3967e3b4effba99c26e2717f31e"
SPOTIFY_CLIENT_SECRET = "f25f70b0ae204ecf8c72d9984ec32494"

### 📌 Film Önerisi Çekme
def get_random_movie():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=tr-TR"
    response = requests.get(url).json()
    
    if "results" not in response or not response["results"]:
        return None
    
    movie = random.choice(response["results"])
    
    return {
        "category": "film",
        "title": movie["title"],
        "description": movie.get("overview", "Açıklama bulunamadı."),
        "rating": movie.get("vote_average", "Bilinmiyor"),
        "year": movie.get("release_date", "Bilinmiyor")[:4],
        "image_url": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
        "source_url": f"https://www.themoviedb.org/movie/{movie['id']}"
    }

### 📌 Dizi Önerisi Çekme
def get_random_series():
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=tr-TR"
    response = requests.get(url).json()

    if "results" not in response or not response["results"]:
        return None
    
    series = random.choice(response["results"])

    return {
        "category": "series",
        "title": series["name"],
        "description": series.get("overview", "Açıklama bulunamadı."),
        "rating": series.get("vote_average", "Bilinmiyor"),
        "year": series.get("first_air_date", "Bilinmiyor")[:4],
        "seasons": series.get("number_of_seasons", "Bilinmiyor"),
        "image_url": f"https://image.tmdb.org/t/p/w500{series.get('poster_path', '')}",
        "source_url": f"https://www.themoviedb.org/tv/{series['id']}"
    }

### 📌 Anime Önerisi Çekme
def get_random_anime():
    url = "https://api.jikan.moe/v4/anime"
    response = requests.get(url).json()

    if "data" not in response or not response["data"]:
        return None

    anime = random.choice(response["data"])

    return {
        "category": "anime",
        "title": anime["title"],
        "description": anime.get("synopsis", "Açıklama bulunamadı."),
        "rating": anime.get("score", "Bilinmiyor"),
        "episodes": anime.get("episodes", "Bilinmiyor"),
        "year": anime.get("aired", {}).get("prop", {}).get("from", {}).get("year", "Bilinmiyor"),
        "image_url": anime["images"]["jpg"]["image_url"],
        "source_url": f"https://myanimelist.net/anime/{anime['mal_id']}"
    }

### 📌 Spotify API Access Token Alma
def get_spotify_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data).json()
    
    return response.get("access_token")

### 📌 Müzik Önerisi Çekme
def get_random_music():
    access_token = get_spotify_access_token()
    if not access_token:
        return {
            "category": "music",
            "title": "Müzik bulunamadı",
            "description": "Spotify API erişim hatası.",
            "image_url": "https://placehold.co/500x500",
            "source_url": "https://spotify.com"
        }

    url = "https://api.spotify.com/v1/browse/new-releases?country=US&limit=10"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers).json()

    if "albums" not in response or "items" not in response["albums"]:
        return None

    song = random.choice(response["albums"]["items"])

    return {
        "category": "music",
        "title": song["name"],
        "description": f"Sanatçı: {', '.join(artist['name'] for artist in song['artists'])}",
        "image_url": song["images"][0]["url"] if song["images"] else "https://placehold.co/500x500",
        "source_url": song["external_urls"]["spotify"]
    }

### 📌 Belgesel Önerisi Çekme
def get_random_documentary():
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=tr-TR&with_genres=99"
    response = requests.get(url).json()

    if "results" not in response or not response["results"]:
        return None

    documentary = random.choice(response["results"])

    return {
        "category": "documentary",
        "title": documentary["title"],
        "description": documentary.get("overview", "Açıklama bulunamadı."),
        "rating": documentary.get("vote_average", "Bilinmiyor"),
        "year": documentary.get("release_date", "Bilinmiyor")[:4],
        "image_url": f"https://image.tmdb.org/t/p/w500{documentary.get('poster_path', '')}",
        "source_url": f"https://www.themoviedb.org/movie/{documentary['id']}"
    }

### 📌 Tüm Önerileri Çeken API Endpoint
def daily_recommendation(request):
    recommendations = [
        get_random_movie(),
        get_random_series(),
        get_random_anime(),
        get_random_music(),
        get_random_documentary()
    ]
    return JsonResponse([r for r in recommendations if r], safe=False)

### 📌 Ana Sayfa Görüntüleme
def home(request):
    return render(request, "index.html")
