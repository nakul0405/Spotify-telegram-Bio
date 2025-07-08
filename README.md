🎧 Spotify–Telegram Bio Updater

**Seamlessly synchronize your Spotify listening activity with your Telegram bio.**

---

## 🧭 Overview

Spotify–Telegram Bio Updater is a lightweight yet dynamic Python script that automatically updates your Telegram bio to reflect the track you're currently playing on Spotify.

By leveraging the Spotify Web API and Telegram’s client API (`Telethon`), this utility bridges your musical taste with your digital presence—elegantly and in real time.

---

## 🔍 Key Features

* 🔄 **Real-Time Updates**: Automatically reflects your current Spotify track in your Telegram bio.
* 🧠 **Intelligent Polling**: Avoids unnecessary API calls by updating only when the song changes.
* 🧱 **Minimal Footprint**: Built with simplicity and efficiency in mind.
* 🛠️ **Fully Configurable**: Customizable update intervals and formatting options.

---

## 🧰 Requirements

* Python 3.7 or higher
* Spotify Developer Credentials (`client_id`, `client_secret`, `refresh_token`)
* Telegram API credentials (`api_id`, `api_hash`)
* A Telegram account

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nakul0405/Spotify-telegram-Bio.git
cd Spotify-telegram-Bio
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Obtain Credentials

#### Spotify:

* Create an app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
* Set a redirect URI (e.g., `https://spotify-refresh-token-generator.netlify.app`).
* Generate a `refresh_token` using the [ Refresh Token Genrator](https://spotify-refresh-token-generator.netlify.app/).

#### Telegram:

* Obtain your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).

---

## 🧩 Configuration

Populate `config.py` or create an `.env` file with the following values:

```python
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REFRESH_TOKEN = "your_spotify_refresh_token"

TELEGRAM_API_ID = 123456  # Integer
TELEGRAM_API_HASH = "your_telegram_api_hash"

POLL_INTERVAL = 15  # in seconds
```

---

## 🚀 Usage

Once configured, simply run:

```bash
python update.py
```

The script will initiate authentication, fetch your current Spotify track, and set your Telegram bio accordingly. It continues to monitor and update in the background based on your `POLL_INTERVAL`.

---

## 🛸 Deployment

This script can be deployed to any always-on environment such as:

### Railway

1. Fork the repository.
2. Connect it to [Railway](https://railway.app/).
3. Set the required secrets in the environment variables.
4. Use `python update.py` as your start command.

---

## ✏️ Example Output

When you're playing:

> `🎧 Now Listening: Kendrick Lamar – HUMBLE.`

When you're not:

> `Currently not playing anything.` *(optional fallback)*

You may customize the bio string format within the code to suit your preferences.

---

## 🧠 Architecture

* **Language**: Python 3.x
* **Libraries**: [`spotipy`](https://spotipy.readthedocs.io/en/2.22.1/), [`telethon`](https://docs.telethon.dev)
* **Polling Loop**: Efficient `asyncio` loop with change detection
* **State Handling**: Prevents redundant API hits by comparing current/previous track state

---

## 🧪 Roadmap & Ideas

* ☑️ Pause/resume detection
* ☑️ Deploy-to-cloud support
* ⬜ Web-based status dashboard
* ⬜ Custom emoji and formatting support
* ⬜ Last.fm support (for non-Spotify users)

---

## 🤝 Contributing

Pull requests are welcome.
If you have suggestions for improvements or new features, feel free to open an issue or fork the repo and submit a PR.

```bash
git checkout -b feature/your-feature
git commit -m "Add your message"
git push origin feature/your-feature
```

---

## 📜 License

This project is licensed under the MIT License.
Feel free to fork, modify, and integrate as long as proper attribution is maintained.

---

## 🌐 Credits

* Creator - [Nakul Rathod](https://t.me/Nakulrathod0405) (Contact If you face any problem or don't know how to deploy the script.)
* Built using APIs provided by [Spotify for Developers](https://developer.spotify.com) and [Telethon](https://github.com/LonamiWebs/Telethon).

---

## ⭐ Show Your Support

If you find this project valuable, give it a ⭐️ on GitHub.
It helps visibility—and fuels future development.
