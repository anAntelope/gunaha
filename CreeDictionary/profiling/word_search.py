import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "CreeDictionary.settings"
django.setup()

from API.models import Inflection

if __name__ == "__main__":
    Inflection.fetch_lemmas_by_user_query("miteh")
