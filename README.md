# 📥 Instagram Downloader API (yt-dlp + FastAPI)

## 🚀 Usage

- Start the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

- Open in browser:

```http
http://localhost:8000/
```

- API Example:

```http
http://localhost:8000/download?url=https://www.instagram.com/reel/xyz123
```

## ⚠️ Notes

- This only works for public Instagram posts.
- It uses `yt-dlp` under the hood.