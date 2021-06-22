import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models  # from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="2", type=int, help="How many rooms you want to create"
        )  # 여기서 default가 의미하는 것?

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()  # Seeder는 Foreign Key로 도울 수 없다.
        all_users = (
            user_models.User.objects.all()
        )  # 다 가져오지만 서비스를 할때는 그닥 좋은 방법은 아니다. (ex: instagram 초기 댓글 표시 갯수)
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),  # faker: 임의의 단어 조합하여 이름 생성
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 8),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 4),
                "bedrooms": lambda x: random.randint(1, 2),
                "baths": lambda x: random.randint(1, 2),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))  # flatten:
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(0, random.randint(5, 8)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",  # URL
                )

            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 3 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(2, 6)
                if magic_number % 2 == 0:
                    room.facilities.add(f)

            for r in rules:
                # magic_number = random.randint(0, 1)
                # if magic_number % 3 == 0:
                room.house_rules.add(r)  # rules는 전부 넣기.

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))