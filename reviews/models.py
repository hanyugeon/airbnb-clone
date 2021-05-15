from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    location = models.IntegerField()
    comminication = models.IntegerField()
    check_in = models.IntegerField()
    cleanliness = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avr = (
            self.accuracy
            + self.location
            + self.comminication
            + self.check_in
            + self.cleanliness
            + self.value
        ) / 6
        return round(avr, 2)  # round() 반올림 함수

    rating_average.short_description = "rating"