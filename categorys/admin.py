from django.contrib import admin
from . import models


@admin.register(models.Book_Genre, models.Movie_Genre)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    pass