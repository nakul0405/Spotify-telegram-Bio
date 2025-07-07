from aiohttp import ClientSession, ClientTimeout
from os import getenv
import base64
import dotenv
import time
import logging

spotify_logger = logging.getLogger("spotify")

dotenv.load_dotenv()

meta = {
    "LAST_UPDATED": time.time(),
    "IS_PLAYING": False,
    "CURRENT_TRACK_TITLE": None,
}

ACTIVE_ACCESS_TOKEN = None
EXPIRATION_TIME = None
UPDATE_INTERVAL = 10

CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")
REFRESH_TOKEN = getenv("SPOTIFY_REFRESH_TOKEN")

BASE_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()}",
}


async def refresh_token():
    spotify_logger.info("<- Refreshing token ->")
    async with ClientSession(timeout=ClientTimeout(total=10)) as session:
        async with session.post(
            "https://accounts.spotify.com/api/token",
            headers=BASE_HEADERS,
            data={
                "grant_type": "refresh_token",
                "refresh_token": REFRESH_TOKEN,
                "client_id": CLIENT_ID,
            },
        ) as response:
            try:
                data = await response.json()
            except Exception as e:
                spotify_logger.error(f"❌ Failed to parse Spotify token response: {e}")
                raise

            if "access_token" not in data:
                spotify_logger.error(f"❌ Spotify token refresh failed: {data}")
                raise Exception("Spotify did not return access_token")

            global ACTIVE_ACCESS_TOKEN
            global EXPIRATION_TIME
            ACTIVE_ACCESS_TOKEN = data["access_token"]
            EXPIRATION_TIME = int(data["expires_in"]) + int(time.time())

    spotify_logger.info("<- Token refreshed ✅ ->")


async def get_current_playing():
    async with ClientSession(timeout=ClientTimeout(total=10)) as session:
        async with session.get(
            "https://api.spotify.com/v1/me/player/currently-playing",
            headers={
                "Authorization": f"Bearer {ACTIVE_ACCESS_TOKEN}",
            },
        ) as response:
            # if status code is 204, no content is playing
            if response.status == 204:
                meta["IS_PLAYING"] = False
                meta["CURRENT_TRACK_TITLE"] = None
                spotify_logger.info("Not currently playing.")
                return

            # if not 200, refresh token and retry
            if response.status != 200:
                spotify_logger.warning(f"Non-200 from Spotify: {response.status} → Refreshing token...")
                await refresh_token()
                return await get_current_playing()

            try:
                data = await response.json()
                if data.get("is_playing"):
                    meta["IS_PLAYING"] = True
                    artists = [artist["name"] for artist in data["item"]["album"]["artists"]]
                    artists_fmt = ", ".join(artists)[:100]
                    meta["CURRENT_TRACK_TITLE"] = f"{data['item']['name']} ({artists_fmt})"
                    spotify_logger.info(f"🎧 Currently playing: {meta['CURRENT_TRACK_TITLE']}")
                else:
                    meta["IS_PLAYING"] = False
                    meta["CURRENT_TRACK_TITLE"] = None
                    spotify_logger.info("Not currently playing.")
            except Exception as e:
                meta["IS_PLAYING"] = False
                meta["CURRENT_TRACK_TITLE"] = None
                spotify_logger.error(f"Error parsing Spotify response: {e}")
