# 🎬 Daily Media Recommendations 🎶

A dynamic Django web application that delivers fresh daily content recommendations across five entertainment categories — **Movies**, **TV Series**, **Anime**, **Music**, and **Documentaries**. Leveraging powerful third-party APIs like **TMDb**, **Spotify**, and **Jikan (MyAnimeList)**, this app fetches real-time data and serves it in a sleek, responsive interface.

---

## 🚀 What It Does

This application helps users discover new media every day. With a single click, it fetches random and trending selections from:

- 🎥 **Movies** – using The Movie Database (TMDb)
- 📺 **TV Series** – also from TMDb
- 🎌 **Anime** – via the Jikan API (unofficial MyAnimeList wrapper)
- 🎵 **Music** – latest albums through Spotify's public API
- 📽 **Documentaries** – filtered from TMDb using genre ID

The homepage is beautifully styled with themed content cards and interactive buttons, encouraging exploration and repeated visits.

---

## ✨ Features at a Glance

- 🔄 **One-click content refresh** – Pulls new recommendations instantly
- 🎨 **Category-themed UI** – Each media type has its own design and color scheme
- ⭐ **Add to Favorites** – Store items temporarily in local session memory
- 📦 **REST API endpoint** – Easily extensible for frontend apps or mobile integration
- 🧠 **Robust Python logic** – Handles API errors, fallbacks, and dynamic rendering

---

## 🧩 Tech Stack

- **Backend:** Django 4+
- **Frontend:** HTML5, CSS3, Vanilla JS
- **APIs Used:**
  - [TMDb API](https://developers.themoviedb.org/)
  - [Spotify API](https://developer.spotify.com/)
  - [Jikan API](https://jikan.moe/)

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/daily-recommendations.git
cd daily-recommendations
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django requests
```

---

## 🔐 API Credentials Setup

Inside `views.py`, replace placeholders with your credentials:

```python
TMDB_API_KEY = "your_tmdb_api_key"
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
```

For production, use `.env` or environment variables with `os.environ.get()`.

---

## 🧪 Running the Project

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔗 API Endpoint

**GET** `/api/recommendations/` returns a list of 5 JSON objects (one per category):

```json
[
  {
    "category": "film",
    "title": "Inception",
    "description": "A thief who steals corporate secrets through dream-sharing...",
    "rating": 8.8,
    "year": "2010",
    "image_url": "https://image.tmdb.org/...",
    "source_url": "https://www.themoviedb.org/movie/27205"
  },
  ...
]
```

---

## 🖼️ User Interface

- **Responsive layout** optimized for desktop and mobile
- **Styled recommendation cards** with category-specific borders and gradients
- **JavaScript-powered interactions**:
  - Load new suggestions
  - Add/view favorites
- **Quotes and animations** for visual appeal

---

## 📁 File Structure

```
├── manage.py
├── recommendations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── templates/
│       └── index.html
```

---

## 🧪 Testing

Basic test suite is scaffolded in `tests.py`. You can extend it to cover:

- View logic
- API error handling
- JSON structure compliance

Run tests:

```bash
python manage.py test
```

---

## 🚀 Deployment Tips

- Set `DEBUG = False` in production
- Use environment variables or a `.env` file for sensitive keys
- Deploy easily to:
  - **Heroku**
  - **Render**
  - **Railway**
  - Or any Django-supported VPS/server

---

## 🪄 Future Ideas

- 💾 User authentication + persistent favorites
- 📊 Recommendation history or analytics
- 📱 Mobile app integration using the same API
- 🔍 Search or filter functionality per category

---

## 📜 License

MIT License © 2025 — Use freely and contribute!

---

## 🙌 Acknowledgements

- [The Movie Database (TMDb)](https://www.themoviedb.org/)
- [Spotify for Developers](https://developer.spotify.com/)
- [Jikan API (MyAnimeList)](https://jikan.moe/)
