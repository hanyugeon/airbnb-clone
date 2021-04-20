from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ week01 User Model """

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

    FAV_BOOK_GENRE_NOVEL = "소설"
    FAV_BOOK_GENRE_ESSAY = "수필(에세이)"
    FAV_BOOK_GENRE_POEM = "시"
    FAV_BOOK_GENRE_PICTURE = "그림책"
    FAV_BOOK_GENRE_COMIC = "만화책"
    FAV_BOOK_GENRE_CHOICES = (
        (FAV_BOOK_GENRE_NOVEL, "소설"),
        (FAV_BOOK_GENRE_ESSAY, "수필(에세이)"),
        (FAV_BOOK_GENRE_POEM, "시"),
        (FAV_BOOK_GENRE_PICTURE, "그림책"),
        (FAV_BOOK_GENRE_COMIC, "만화책"),
    )

    FAV_MOVIE_GENRE_ACTION = "액션"
    FAV_MOVIE_GENRE_SF = "SF(공상과학)"
    FAV_MOVIE_GENRE_COMEDY = "코미디"
    FAV_MOVIE_GENRE_THRILLER = "스릴러"
    FAV_MOVIE_GENRE_WAR = "전쟁"
    FAV_MOVIE_GENRE_SPORTS = "운동"
    FAV_MOVIE_GENRE_FANTASY = "판타지"
    FAV_MOVIE_GENRE_MUSIC = "음악"
    FAV_MOVIE_GENRE_MELLO = "멜로"
    FAV_MOVIE_GENRE_CHOICES = (
        (FAV_MOVIE_GENRE_ACTION, "액션"),
        (FAV_MOVIE_GENRE_SF, "SF(공상과학)"),
        (FAV_MOVIE_GENRE_COMEDY, "코미디"),
        (FAV_MOVIE_GENRE_THRILLER, "스릴러"),
        (FAV_MOVIE_GENRE_WAR, "전쟁"),
        (FAV_MOVIE_GENRE_SPORTS, "운동"),
        (FAV_MOVIE_GENRE_FANTASY, "판타지"),
        (FAV_MOVIE_GENRE_MUSIC, "음악"),
        (FAV_MOVIE_GENRE_MELLO, "멜로"),
    )

    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)

    preference = models.CharField(
        choices=PREFERENCE_LV_CHOICES, max_length=4, null=True, blank=True  # choices
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=4, null=True, blank=True
    )

    favorite_book_genre = models.CharField(
        choices=FAV_BOOK_GENRE_CHOICES, max_length=20, null=True, blank=True
    )

    favorite_movie_genre = models.CharField(
        choices=FAV_MOVIE_GENRE_CHOICES, max_length=20, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)

    """
    Custom User Model

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True  # choices
    )

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)  # DateField
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
    
    """