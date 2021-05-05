from django.db import models
from core import models as core_models

# from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Book_Genre(AbstractItem):

    """ Book_Genre Model Definition """

    class Meta:
        verbose_name = "Book Genre"


class Movie_Genre(AbstractItem):

    """ Movie_Genre Model Definition """

    class Meta:
        verbose_name = "Movie Genre"


class Category(core_models.TimeStampedModel):

    """ Category Model Definition """

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

    favorite_book_genre = models.CharField(
        choices=FAV_BOOK_GENRE_CHOICES, max_length=20, blank=True
    )

    favorite_movie_genre = models.CharField(
        choices=FAV_MOVIE_GENRE_CHOICES, max_length=20, blank=True
    )