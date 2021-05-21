import os

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo.settings')
django.setup()
fake = Faker()

from tasks.models import Task


def populate_tasks(param):
    for x in range(param):
        title = fake.company()
        Task.objects.get_or_create(title=title[:20])


if __name__ == '__main__':
    print("populating script!")
    populate_tasks(30)
    print("population complete")
