from django.shortcuts import render
from . import models

def all_rooms(request): # 04 core_urls.py에 all_rooms입력
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={
        "potato": all_rooms # potato에 주목, templets_home.html 과 비교
    })