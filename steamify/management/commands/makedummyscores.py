from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from steamify.models import ALL_COMPETS, Team, AeroMiddle, Spont
import csv
import os
from steamify.utils.misc import getUserDisplayedAttrs
from typing import List
import random
from django.utils import timezone



def getRandJudge():
    return random.choice(list(User.objects.all())[1:5])
    # return User.objects.get(
    #            username=random.choice(
    #                ["cplantz", "agess", "vcox", "acruz"]))


def getRandTeam():
    return random.choice(list(Team.objects.all())[17:23])


def getCommonDeets():
    return {
        "judge": getRandJudge(),
        "team": getRandTeam(),
        "created_at": timezone.now()
    }


def getCompetSpecific(Compet):
    scoreable = getUserDisplayedAttrs(Compet)  # type: List[str]
    return dict(
        (x, random.randint(1, 5))
        for x in scoreable
    )


def makeDummyScores(Compet):
    """for one competition"""
    # import ipdb; ipdb.set_trace()
    deets = getCommonDeets()
    deets.update(getCompetSpecific(Compet))
    scoreEntry = Compet(**deets)
    scoreEntry.save()
    print(deets)    


def makeDummyScoresAllCompets():
    for unused in range(3):
        makeDummyScores(AeroMiddle)
        makeDummyScores(Spont)
    # for Compet in ALL_COMPETS:
        # makeDummyScores(Compet)


class Command(BaseCommand):

    def handle(self, *args, **options):
        makeDummyScoresAllCompets()
        