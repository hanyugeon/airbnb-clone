from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # UserAdmin? (ctrl + 클릭)
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ week01 User Admin """

    fieldsets = UserAdmin.fieldsets + (  # UserAdmin.fieldsets + ... 무슨 뜻인지 인지하기.
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

    list_display = (  # 유저 리스트 보여주기
        "username",
        "email",
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
        "superhost",
    )

    list_filter = (  # 유저 항목별 필터 추가
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
    )