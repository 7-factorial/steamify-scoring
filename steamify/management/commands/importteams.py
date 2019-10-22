from django.core.management.base import BaseCommand
from steamify.models import Team
import csv
import os


def readOneFile(fpath):
    with open(fpath, encoding="utf_8_sig") as f:
        reader = csv.DictReader(f)
        for line in reader:
            Team.objects.create(
                dotted_id=line["dotted_id"].strip(),
                name=line["name"].strip(),
                school_name=line["school_name"].strip(),
                )


class Command(BaseCommand):

    def handle(self, *args, **options):
        readOneFile(os.path.join("miscdata", "teamData.csv"))
        