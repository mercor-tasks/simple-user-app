from utils.exceptions import NotFoundError

from .models import SiteUser


def get_user_by_username(username: str) -> SiteUser:
    filtered = SiteUser.objects.filter(username=username)
    if not filtered.exists():
        raise NotFoundError(f"User with {username} doesn't exist")
    return filtered.first()
