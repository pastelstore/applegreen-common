import jwt

from datetime import datetime, timedelta
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from applegreen_common.constant.constant import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS, ALGORITHM
from .encryption import get_secret_key

# get cached secret key
secret_key = get_secret_key()


def create_access_token(data: dict, expire_delta: timedelta | None = None) -> str:
    if secret_key is None:
        raise RuntimeError("Secret key NOT loaded.")

    # 데이터 변형을 위한 복사
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    if secret_key is None:
        raise RuntimeError("Secret key NOT loaded.")

    # 데이터 변형을 위한 복사
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)


def decode_token(token: str) -> dict | None:
    if secret_key is None:
        raise RuntimeError("Secret key NOT loaded.")

    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return {
            "store_id": payload.get("store_id", None),
            "user_id": payload.get("user_id", None),
            "seller_id": payload.get("seller_id", None)
        }

    except ExpiredSignatureError:
        return None

    except InvalidTokenError:
        return None
