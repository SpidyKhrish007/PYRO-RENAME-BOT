import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23830477")

API_HASH = os.environ.get("API_HASH", "19f8365d98fb11c9cd6c1eaa8b1fa4b8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6074196500:AAFT2yBAui79EQMJ9PrbA55Usf9o8bUbgoQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Cluster1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Khrish:<12121212>@cluster1.hh7bbcz.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
