from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # UserAdmin? (ctrl + 클릭)
from . import models

# Register your models here.


@admin.register(models.User)
class UsersAdmin(UserAdmin):

    """ week01 User Admin """

    # admin.py가 패널의 구성을 바꿀 수 있다.
    fieldsets = UserAdmin.fieldsets + (  # UserAdmin.fieldsets + ... 무슨 뜻인지 인지하기.
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "preference",
                    "language",
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
        "superhost",
    )

    list_filter = (  # 유저 항목별 필터 추가
        "preference",
        "language",
    )