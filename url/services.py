from django.utils.crypto import get_random_string


def generate_short_url(length: int=8) -> str:
    return get_random_string(length)
