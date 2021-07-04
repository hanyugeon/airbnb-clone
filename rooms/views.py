from math import ceil
from django.shortcuts import render
from . import models

def all_rooms(request): # 04 core_urls.py에 all_rooms입력
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request, 
        "rooms/home.html",
        {
            "potato": all_rooms, # potato에 주목, templets_home.html 과 비교
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1)
        }
    )