# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem

class Command(BaseCommand):
    help = u"Read tasks from file (one line = one task)and save them to db"

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='input_file', type=str)

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        deriction = 'in'
        with open(f'tasks\management\commands\{options["input_file"]}', 'r', encoding='UTF-8') as text:
            for i in text:
                t = TodoItem(description=i, created=now)
                t.save()
                