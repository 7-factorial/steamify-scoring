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


def _readOneFile(fpath):

    teamDataFromFile = list(_getDataFromFile(fpath))

    for teamdat in teamDataFromFile:
        Team.objects.create(**teamdat)


def _createFakeTeam():
    try:
        Team.objects.create(
            dotted_id="M.RO.999",
            name="Fake team for testing",
            school_name="Fake"
        )
    except Exception as e:
        print("Minor warning:"
            "Tried to create a fake team called"
            "M.RO.999"
            "But was unable to for some reason:")
        print(e)


class Command(BaseCommand):

    def handle(self, *args, **options):
        _readOneFile(os.path.join("miscdata", "teamData.csv"))
        _createFakeTeam()
