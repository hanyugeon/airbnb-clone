from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # UserAdmin? (ctrl + 클릭)
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # admin.py가 패널의 구성을 바꿀 수 있다.
    fieldsets = UserAdmin.fieldsets + (  # UserAdmin.fieldsets + ... 무슨 뜻인지 인지하기.
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (  # 유저 리스트 보여주기
        "username",
        "first_name",
        "last_name",
        "gender",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
