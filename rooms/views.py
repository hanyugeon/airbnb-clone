from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

def all_rooms(request): # 04 core_urls.py에 all_rooms입력
    page = request.GET.get("page", 1)  # "page" / "page", 1 페이지가 존재하지 않을경우 default 값 1을 가져옴.
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))    # get_page(page) / page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")