from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates houserules"

    """
    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many time do you want me")
    """

    def handle(self, *args, **options):
        houserules = [
            "do not smoke", 
            "repair it", 
            "put it back", 
            "clean it", 
            "turn it off", 
            "close it", 
            "return it ", 
            "keep it"
        ]
        for r in houserules:  # 여기서 r는 houserules 배열안에 있는 str 들을 가리킴
            HouseRule.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(houserules)} created!"))