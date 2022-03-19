from django.core.management.base import BaseCommand

import os
import csv
import string
import copy


def _is_basic_ascii_char(char):
    return (char in string.ascii_lowercase)


def _clean(name):
    lo = name.lower()

    # Omit periods, quotation marks, etc
    return "".join(filter(_is_basic_ascii_char, lo))


def _makeUsernameIfNeeded(line):
    if line["username"]:
        return line  # no change
    
    # John Doe => jdoe
    firnam = _clean(line["first_name"])
    lasnam = _clean(line["last_name"])

    un = firnam[0] + lasnam[0:4+1]

    newLine = copy.copy(line)
    newLine["username"] = un
    return newLine


def _reportDupes(newLines):
    usernames = [line["username"] for line in newLines]
    dupes = set(x for x in usernames if usernames.count(x) > 1)
    if dupes:
        raise ValueError("Found duplicate usernames: {}; please add manual overrides for those names in rawjudgeData.csv".format(dupes))


def _doit():
    sourcefpath = os.path.join("miscdata", "rawjudgeData.csv")
    destfpath =  os.path.join("miscdata", "judgeData.csv")

    with open(sourcefpath) as f:
        oldLines = list(csv.DictReader(f))

    newLines = list(map(_makeUsernameIfNeeded, oldLines))

    # if newLines == oldLines:
        # no need to write to file if it didn't change.
        # return

    _reportDupes(newLines)

    with open(destfpath, "w") as f:
        writer = csv.DictWriter(f, fieldnames=
            ["first_name", "last_name", "username"])
        writer.writeheader()
        writer.writerows(newLines)
        



class Command(BaseCommand):

    def handle(self, *args, **options):    
        
        _doit()
