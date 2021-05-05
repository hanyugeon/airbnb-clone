from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser? (ctrl + 클릭)

# Create your models here.


class User(AbstractUser):

    """ User Model Definition """

    PREFERENCE_LV_01 = "1"
    PREFERENCE_LV_02 = "2"
    PREFERENCE_LV_03 = "3"
    PREFERENCE_LV_04 = "4"
    PREFERENCE_LV_05 = "5"
    PREFERENCE_LV_CHOICES = (
        (PREFERENCE_LV_01, "1"),
        (PREFERENCE_LV_02, "2"),
        (PREFERENCE_LV_03, "3"),
        (PREFERENCE_LV_04, "4"),
        (PREFERENCE_LV_05, "5"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    avatar = models.ImageField(blank=True)
    bio = models.TextField(default="", blank=True)

    preference = models.CharField(
        choices=PREFERENCE_LV_CHOICES, max_length=4, blank=True  # choices
    )

    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=4, blank=True)

    superhost = models.BooleanField(default=False)
