from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("name",)

    filter_horizontal = ("rooms",)  # rooms > admin.py 에 있는 filter_horizontal 가져옴.
