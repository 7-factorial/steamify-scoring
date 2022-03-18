from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mysite.envconfig import get_judge_pw

import csv
import os


def readOneFile(fpath):
    with open(fpath) as f:
        reader = csv.DictReader(f)
        for line in reader:
            un = line["username"].strip()
            if not un:
                raise ValueError("Empty username. Either edit the judgeData.csv directly, or use the makeUsernames command.")
            if User.objects.filter(username=un).exists():
                raise ValueError("username already exists: {}".format(un))
            
            dat = {
                "username": un,
                "first_name": line["first_name"].strip(),
                "last_name": line["last_name"].strip(),
                "password": get_judge_pw(un)
            }
            
            User.objects.create_user(**dat)


class Command(BaseCommand):

    def handle(self, *args, **options):
        readOneFile(os.path.join("miscdata", "judgeData.csv"))
        