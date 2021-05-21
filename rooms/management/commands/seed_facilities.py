from django.core.management.base import BaseCommand
from rooms.models import Facility  # from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates facilities"

    """
    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many time do you want me")
    """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:  # 여기서 a는 amenities 배열안에 있는 str 들을 가리킴
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} created!"))