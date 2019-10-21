from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mysite.envconfig import get_judge_pw

import csv
import os


def readOneFile(fpath):
    with open(fpath, encoding="utf_8_sig") as f:
        reader = csv.DictReader(f)
        for line in reader:
            dat = {
                "username": line["username"].strip(),
                "first_name": line["first_name"].strip(),
                "last_name": line["last_name"].strip(),
            }
            if User.objects.filter(username=dat["username"]).exists():
                print("username already exists: {}".format(dat["username"]))
            else:
                dat["password"] = get_judge_pw(dat)
                User.objects.create_user(**dat)


class Command(BaseCommand):

    def handle(self, *args, **options):
        readOneFile(os.path.join("miscdata", "judgeData.csv"))
        