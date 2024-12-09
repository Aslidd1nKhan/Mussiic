#MIT License

#Audiomusiccstreaming (Telegram Voice Chat Bot)
#Credits @subinps, @dashezup and @AsmSafone
#Copyright (C) brut-ctrl <https://github.com/brut-ctrl>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
C_PLAY=False
Y_PLAY=False
STREAM=os.environ.get("STREAM_URL", "https://t.me/zoirjons_music/3")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
regex_ = r"http.*"
match_ = re.match(regex_,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[-1]
elif STREAM.startswith("https://t.me/zoirjons_music/3"):
    try:
        msg_id=STREAM.split("/", 4)[4]
        finalurl=int(msg_id)
        Y_PLAY=True
    except:
        finalurl="https://t.me/zoirjons_music/3"
        print("Unable to fetch youtube playlist, starting Denger.in FM")
        pass
elif match_:
    finalurl=STREAM 
else:
    C_PLAY=True
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '6272205785 7102775549')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '7363937'))
    CHAT = int(os.environ.get("CHAT", "-1002247685563"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1002427657525")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    CPLAY=C_PLAY
    YPLAY=Y_PLAY
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    DELETE_HISTORY=bool(os.environ.get("DELETE_HISTORY", True))
    LIMIT=int(os.environ.get("LIMIT", 1500))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "F")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 60))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "16778e88a5e553e9c3daf389436c6c45")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7862732765:AAEGFhJGWb26nNy6GKgd1TChHxMoyrq4ZEU")     
    SESSION = os.environ.get("SESSION_STRING", "AgE6vl8ASZdaDO_doc3H6YPz6jLTMNIjjRRUVVNuLBo5YBMKyB5nX0v5J0e_LpfVDWt2V3wLMW0Qk9UXTIg6Kwt-CM0Kt6NpxOsain3-eeV35Mx8-ibEivuKTnSOEy9rhXNg1jMOmRCnEfNCIm9QM5dnkJulTVZkvOiTFDLtXHdiy8BsFGVazFlgm3r6D2S5lxzuvozf8OKDd4evDFIW2fYYJmCc9Sn9uX-_GRtd8fcPrhYluTJBQIoHi4QbQ5S_7xWqMxsqp93Ru64cRPlMi6QQF734nVQNj_09BtJLwgMiaPC9g3AmSvxxYanr2kA2Ilo7FFVfhg3-oMIYbcUOHcDqjX6ZrgAAAAGnW8D9AA")
    playlist=[]
    msg = {}
    CONV = {}

