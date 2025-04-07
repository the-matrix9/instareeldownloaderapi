from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, HTMLResponse
from yt_dlp import YoutubeDL
import uvicorn

app = FastAPI(title="Instagram Downloader API", docs_url=None, redoc_url=None)

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <h1>📥 Instagram Downloader API</h1>
    <p>Use this API to download Instagram videos, reels, and images using <code>yt-dlp</code>.</p>
    <h2>🛠️ Usage:</h2>
    <pre>/download?url=INSTAGRAM_POST_URL</pre>
    <h3>🔗 Example:</h3>
    <pre>/download?url=https://www.instagram.com/reel/xyz123</pre>
    <h2>⚠️ Note:</h2>
    <ul>
        <li>Make sure the post is public.</li>
        <li>This uses yt-dlp under the hood.</li>
    </ul>
    """

@app.get("/download")
async def download(url: str = Query(..., description="Instagram Post URL")):
    ydl_opts = {"skip_download": True, "quiet": True, "forcejson": True}
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
                "uploader": info.get("uploader"),
                "formats": [
                    {
                        "format": f.get("format"),
                        "ext": f.get("ext"),
                        "quality": f.get("format_note"),
                        "url": f.get("url")
                    }
                    for f in info.get("formats", [])
                    if f.get("url")
                ]
            }
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)