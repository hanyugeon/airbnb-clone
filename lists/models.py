from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definitions """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()   # count() 메소드

    count_rooms.short_description = "Number of Rooms"  # .short_description 이름 바꿔 줌
