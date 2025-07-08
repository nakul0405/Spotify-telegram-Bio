🎧 Spotify × Telegram Bio Updater

Real-time Spotify track → Your Telegram bio. Fully automated. Super slick. Just hit play. 🔄

 <!-- Optional GIF/banner -->


---

⚡ What Is This?

Every time you play a song on Spotify...

> 🎶 Your Telegram bio updates itself — live — to match your current jam.



Simple. Personal. Dynamic. 🔥


---

✨ Features

⏱️ Auto-updates your bio every few seconds.

🔍 Only updates when the song changes.

📱 Shows track name + artist.

💾 Light, fast, and super easy to set up.

🧠 Built with Python, Spotify API & Telethon.



---

📸 Demo

> Listening to: Blinding Lights – The Weeknd
(Updated in Telegram bio automatically)




---

🧰 Requirements

✅ Python 3.7+

✅ Spotify Developer Account (Client ID/Secret)

✅ Telegram API credentials (api_id & api_hash)

✅ One-time session authentication



---

🛠️ Setup in 3 Steps

1. Clone & Install

git clone https://github.com/nakul0405/Spotify-telegram-Bio.git
cd Spotify-telegram-Bio
pip install -r requirements.txt

2. Get Your Credentials

🔐 Spotify:

Go to Spotify Developer Dashboard

Create an app → get your client_id and client_secret

Set redirect URI to: http://localhost:8888/callback

Generate your refresh_token using the helper script (check /auth/ folder if available)


💬 Telegram:

Go to my.telegram.org

Get your api_id and api_hash

Login once to create a .session file


3. Configure

Create a .env or fill in config.py like this:

SPOTIFY_CLIENT_ID = "your-client-id"
SPOTIFY_CLIENT_SECRET = "your-client-secret"
SPOTIFY_REFRESH_TOKEN = "your-refresh-token"

TELEGRAM_API_ID = 123456
TELEGRAM_API_HASH = "your-telegram-api-hash"

POLL_INTERVAL = 15  # in seconds


---

🧪 Run It!

python update.py

Boom 💥
Your Telegram bio now lives in sync with your Spotify soul.


---

🌍 Deploy Anywhere

Wanna keep it running 24/7?

🚀 Railway

Fork this repo

Link to Railway

Add your secrets in Environment Variables

Set command: python update.py

Done. Your bot is now cloud-powered ☁️



---

💡 Customization Ideas

🎨 Add emoji, artist-only, or album info

💤 Add fallback bio when nothing is playing

🔁 Cycle through lyrics, timestamps, moods

🔊 Use Last.fm if you don’t use Spotify



---

🧙‍♂️ Code Magic

Built with:
💠 Python 3

🟢 Spotify Web API (spotipy)

📨 Telethon (Telegram client)

🧠 Async event loop for smooth updates



---

💬 Example Bio Formats

Status	Telegram Bio

🎵 Playing track	🎧 Listening to: Artist - Song
💤 Nothing playing	`Idle
⌛ Paused	Paused: Track Name



---

🤝 Contribute

Want to add dark mode? CLI args? GUI?
Pull requests are welcome! Fork it and go crazy. 🛠️

git checkout -b new-feature
git commit -m "Added awesome feature"
git push origin new-feature


---

📄 License

MIT License © Nakul0405
Do what you want, just don’t forget to vibe responsibly. 🎶


---

📢 Shoutouts

Thanks to Spotify & Telethon



---

💚 Like It?

Give it a ⭐️ on GitHub
Play your music proudly. 
Let your Telegram bio do the talking. 
