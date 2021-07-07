from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")] # 03
# views.py 에 있는 def, all_rooms와 일치해야 함