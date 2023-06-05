import os
import django

# set the DJANGO_SETTINGS_MODULE env variable to the "url_shortner.settings" module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "url_shortener.settings")

# Initialize the Django framework
django.setup()

# Import the URLShortener class from the url_shortener_app pckg
from url_shortener_app.url_shortener import URLShortener

if __name__ == '__main__':
    shortener # placeholder for further code