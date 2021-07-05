from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request): # 04 core_urls.py에 all_rooms입력
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms": rooms})