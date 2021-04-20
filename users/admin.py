from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ week01 User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "preference",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
        "superhost",
    )

    list_filter = (
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
    )

    """
    Custom User Admin 
    fieldsets = UserAdmin.fieldsets + (  # blue something(파랭이)
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    """
