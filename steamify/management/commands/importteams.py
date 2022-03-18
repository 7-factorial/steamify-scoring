from django.core.management.base import BaseCommand
from steamify.models import Team
import csv
import os



def _getDataFromFile(fpath):
    with open(fpath) as f:
        reader = csv.DictReader(f)
        for line in reader:
            yield {
                "dotted_id": line["dotted_id"].strip(),
                "name": line["name"].strip(),
                "school_name": line["school_name"].strip(),
            }
   

## Unnecessary; this check is done elsewhere
# def _runChecks(teamDataFromFile):
#     def _num(x):
#         a, b, c = x["dotted_id"].split(".")
#         return int(c)

#     nums = list(map(_num, teamDataFromFile))
#     assert len(set(nums)) == len(nums)


def readOneFile(fpath):
     
    teamDataFromFile = list(_getDataFromFile(fpath))

    for teamdat in teamDataFromFile:
        Team.objects.create(**teamdat)


class Command(BaseCommand):

    def handle(self, *args, **options):
        readOneFile(os.path.join("miscdata", "teamData.csv"))
        