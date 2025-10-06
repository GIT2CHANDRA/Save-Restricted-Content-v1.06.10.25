import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7968541029:AAGJny-nCGHXgezJkmI9Xgn3nVruFROBy7U")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18347724"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bcac87df3b75ecc096a1c1b83975ee77")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1301492049"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://besib69802:YMOfgvnyjbRgW5qt@cluster0.yzzu2gn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
