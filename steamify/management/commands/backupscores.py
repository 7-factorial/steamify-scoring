from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from steamify.models import ALL_COMPETS, Shared
from steamify.utils.misc import getUserDisplayedFields
import time

import csv
import os


def procOneEntry(entry):
    # type: (Shared) -> dict
    fds = entry._meta.get_fields()
    # source in case I want to double check: https://stackoverflow.com/questions/51905712/how-to-get-the-value-of-a-django-model-field-object
    return dict((f.name, getattr(entry, f.name)) for f in fds if f.name != "shared_ptr")


def recordOne(Compet, fpath):
    with open(fpath, "w", newline="") as f:
        rows = [procOneEntry(x) for x in Compet.objects.all()]
        
        if not rows:
            return

        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def runOnce():
    partialname = "backup_{}".format(int(time.time()))
    timestampRoot = os.path.join("miscdata", partialname)
    os.mkdir(timestampRoot)
    for Compet in ALL_COMPETS:
        fpath = os.path.join(timestampRoot, Compet.__name__ + ".csv")
        recordOne(Compet, fpath)


def doit():
    while True:
        pc = time.perf_counter()
        runOnce()
        print("Backed up in", time.perf_counter() - pc, "secs")
        time.sleep(5*60)


class Command(BaseCommand):

    def handle(self, *args, **options):
        doit()
        