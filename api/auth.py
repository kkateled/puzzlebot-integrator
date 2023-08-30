import jwt  # used for encoding and decoding jwt tokens
from datetime import datetime, timedelta  # used to handle expiry time for tokens
from passlib.context import CryptContext  # used for hashing the password
from fastapi import HTTPException  # used to handle error handling
from api.config.global_config import GlobalConfig


global_config = GlobalConfig()


class Auth:
    hasher = CryptContext(schemes=["bcrypt"])
    security = global_config.security

    def encode_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, encoded_password):
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=int(self.security.access_token_ttl)),
            'iat': datetime.utcnow(),
            'scope': 'access_token',
            'sub': username
        }
        return jwt.encode(
            payload,
            self.security.secret_key,
            self.security.algorithm)

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.security.secret_key, algorithms=[self.security.algorithm])
            if payload['scope'] == 'access_token':
                return payload['sub']
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def encode_refresh_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=int(self.security.refresh_token_ttl)),
            'iat': datetime.utcnow(),
            'scope': 'refresh_token',
            'sub': username
        }
        return jwt.encode(
            payload,
            self.security.secret_key,
            self.security.algorithm)

    def refresh_token(self, refresh_token):
        try:
            payload = jwt.decode(refresh_token, self.security.secret_key, algorithms=[self.security.algorithm])
            if payload['scope'] == 'refresh_token':
                username = payload['sub']
                new_token = self.encode_token(username)
                return new_token
            raise HTTPException(status_code=401, detail='Invalid scope for token')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Refresh token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid refresh token')


auth_handler = Auth()


def get_session_user(credentials, curd, db):
    access_token = credentials.credentials
    if access_token is None:
        return HTTPException(status_code=401, detail='Forbidden')
    user = crud.get(db, identificator=auth_handler.decode_token(access_token))
    if user is None:
        return HTTPException(status_code=401, detail='User not found')