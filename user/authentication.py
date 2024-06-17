from .models import CustomUser
from datetime import timedelta, datetime, timezone
from django.conf import settings 
from .repository import CustomUserRepository
import jwt



def authenticate(username, password):
    username_dict = {"username": username}
    user = CustomUserRepository.filter_user(username_dict)
    user = list(user)

    if len(user) > 0:
        if password==user[0].password:
            return user[0]
    return None

def generate_token(user):
    payload = {
        'username': user.username,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=10)
    }
    return jwt.encode(payload=payload,
                      key=getattr(settings, "SECRET_KEY"),
                      algorithm='HS256')

def refresh_token(user):
    return generate_token(user)

def verify_token(token):
    error_code = 0
    payload = None

    try:
        payload = jwt.decode(jwt=token,
                      key=getattr(settings, "SECRET_KEY"),
                      algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        error_code = 1
    except jwt.InvalidTokenError:
        error_code = 2
    return [error_code, payload]

def get_authenticated_user(token):
    _, payload = verify_token(token)

    if payload is not None:
        username_dict = {"username": payload['username']}
        user = CustomUserRepository.filter_user(username_dict)
        if len(user) > 0:
            return user[0]