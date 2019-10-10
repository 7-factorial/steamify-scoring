from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from typing import List, Type
from django.utils import timezone

# Create your models here.
from django.urls import reverse

from .utils.misc import makeEditLink


# def rangeTuple(start, endInclusive):
#     return [(x, str(x)) for x in range(start, endInclusive + 1)]


def labeledRangeTuple():
    return [
        (1, "1 (lowest)"),
        (2, "2"),
        (3, "3 (meets described standards)"),
        (4, "4"),
        (5, "5 (exceeds described standards)")
    ]


def standardSteamifyField(help_text_unproc, verbose_name=None):
    return models.IntegerField(
        choices=labeledRangeTuple(),
        help_text=htmlListify(help_text_unproc),
        verbose_name=verbose_name)
    

def htmlListify(rawstr):
    # type: (str) -> str
    spl = rawstr.splitlines()
    stripped = [x.strip() for x in spl]
    noEmpties = [x for x in stripped if x]
    with_lis = "\n".join(format_html("<li>{}</li>", x) for x in noEmpties)
    return "<ul>{}</ul>".format(with_lis)


def verify_team_id_before_creating(teamObj):
    # type: (Team) -> None

    dotid = teamObj.dotted_id  # type:str
            
    # if it doesn't have 2 dots, then this will fail
    gradeletter, subject, numericalpart = dotid.split(".")
    
    if gradeletter not in ("E", "M"):
        raise ValueError("Team id must start with E or M")
    
    thisTla = gradeletter + "." + subject
    TLAS = [x.TLA for x in ALL_EXCEPT_SPONT]
    if thisTla not in TLAS:
        raise ValueError("{} does not appear to be a valid TLA".format(thisTla))

    try:
        existing = Team.objects.get(dotted_id__endswith=numericalpart)                
    except Team.DoesNotExist:
        pass  # The good case is not finding a team with that number.
    else:
        raise ValueError("The numerical portion '{}' already exists: '{}'. All numbers must be unique".format(numericalpart, existing.dotted_id))    


class Team(models.Model):
    dotted_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=300)
    school_name = models.CharField(max_length=300)

    def __str__(self):
        return "{}: '{}' ({})".format(self.dotted_id, self.name, self.school_name)
    
    def save(self, *args, **kwargs):        
        if self._state.adding:
            verify_team_id_before_creating(self)

        super().save(*args, **kwargs)  # Call the "real" save() method.


class Shared(models.Model):
    # something_shared = models.IntegerField(
    #     choices=labeledRangeTuple(),
    #     help_text="Did they do somethign well that involes all competitions?")
    TLA = "Shared_class_which_only_has_TLA_to_avoid_exceptions"
    spontOrLong = "long"  # override this in spont
    judge = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        )
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        )
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if self._state.adding:
            self.created_at = timezone.now()
        else:
            self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Score: {}, {} (BehindTheScenesID={})".format(self.judge, self.team.dotted_id, self.pk)
    
    def get_absolute_url(self):
        # type: (...) -> str
        # TODO (I think this works, but a bit more testing would be nice)
        return makeEditLink(self.TLA, {
            'spontOrLong': self.spontOrLong,
            'full_team_id': self.team.dotted_id,
            'pk': self.pk})


    # maybe TODO? add grade_and_category

    # TODO: save must check if there's already an entry for
    #   that judge
    #   that team
    #   that competition
    # If there is, then... Display an error and say "Are you trying to edit your submission?" then give a link
    # However there's an inevitable race condition.
    # ANOTHER TODO: On the server side, every minute or so, check if there's a double entry (criteria above).
    # If it's same score, delete the oldest one
    # If it's different score, display on like a problem report. (presumably the person submitted twice quickly, OR they used the back button and submitted again)
    # In fact, here's a way to do that:
    # I (Jaime) will have a status page for myself which every 20 seconds sends a json request
    # that will trigger the double-entry check and give some other status stuff (not yet decided what the other status stuff is).


# each instance of this will be a single score submission by one judge
class EngMiddle(Shared):
    TLA = "M.EN"
    presentation = standardSteamifyField("""
        Presentation demonstrates understanding of the material.
        Presenters facilitate engaging discussion regarding challenge expectations.  
        Presenters explain their research concerning the CO2 device as it relates to environmental sustainability.
        The purpose of the design is clear, realistic, and presenters share how it may be scaled up.
        Most students have an explicit part in either the explanation or demonstration of the design process regarding the prototype; however, one or two may function as support.
        """)
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
    engineering_design_prototype_working_model = standardSteamifyField("""
        The operation and design of the prototype somewhat fulfill the challenge, but is unclear in some aspects.
        """, verbose_name="Engineering Design/Prototype/Working Model")
    engineering_statement = standardSteamifyField("""
        Written statement submitted at the time of performance.
        Statement is neat and has 1-3 spelling/grammatical/punctuation errors.
        Statement links standards to key elements and outcome, but may be unclear in one or two places.""")
    

class EngElem(Shared):
    TLA = "E.EN"


class VisualArtsMiddle(Shared):
    TLA = "M.VA"
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class VisualArtsElem(Shared):
    TLA = "E.VA"
    artistic_artsyness = standardSteamifyField("""Are they artsy? OR Fartsy?""")


class AeroMiddle(Shared):
    TLA = "M.AE"


class DanceMiddle(Shared):
    TLA = "M.DA"


class DanceElem(Shared):
    TLA = "E.DA"


class DebateMiddle(Shared):
    TLA = "M.DE"


class RocketMiddle(Shared):
    TLA = "M.RO"


class SpokenMiddle(Shared):
    TLA = "M.SW"


class SpokenElem(Shared):
    TLA = "E.SW"


class TheaterMiddle(Shared):
    TLA = "M.TH"


class TheaterElem(Shared):
    TLA = "E.TH"



# TODO: is there a spont middle and a spont elem rubric?
class Spont(Shared):
    TLA = "FAKE_TLA_FOR_SPONT"
    # # There shouldn't be a TLA for Spont because all teams have another category; 
    #  BUT TODO: I need to check where TLA is used to make sure I don't assume 1-to-1 
    # and therefore break Spont
    spontOrLong = "spont"
    specific_to_spontaneous = standardSteamifyField("""
    Words about things.
    This also says this.
    """)



# VERIFIED 2019 Oct 7 at 5:02 pm - this contains all competitions
ALL_EXCEPT_SPONT = [EngMiddle, EngElem, VisualArtsMiddle, VisualArtsElem,
                    AeroMiddle, DanceMiddle, DanceElem, DebateMiddle, 
                    RocketMiddle, SpokenMiddle, SpokenElem, TheaterMiddle,
                    TheaterElem]  # type: List[Type[Shared]]

# TODO: add spont if it ends up being useful
ALL_COMPETS = ALL_EXCEPT_SPONT + [Spont]
