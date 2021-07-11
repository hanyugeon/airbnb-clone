from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
# rooms/view.py def room_detail(arguments(include pk!!!))