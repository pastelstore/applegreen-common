import os

from dotenv import load_dotenv

# load .env
load_dotenv()

# db 접속 정보
AG_DB = f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
AG_DB_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
         f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"

# jwt
SECRET_KEY_PATH = os.getenv("SECRET_KEY_PATH")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7
ALGORITHM = "HS256"

# api uri
STORE_API_URI = os.getenv("STORE_API_URI")
