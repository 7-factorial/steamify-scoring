from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html


# Create your models here.
from django.urls import reverse



# def rangeTuple(start, endInclusive):
#     return [(x, str(x)) for x in range(start, endInclusive + 1)]


def labeledRangeTuple():
    return [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
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


class Team(models.Model):
    dotted_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return "'{}' ({})".format(self.name, self.dotted_id)




class Shared(models.Model):
    # something_shared = models.IntegerField(
    #     choices=labeledRangeTuple(),
    #     help_text="Did they do somethign well that involes all competitions?")
    judge = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        )

    def __str__(self):
        return "Score entry for {} (NEED TEAM ID) judged by {}".format(self.TLA, self.judge)
    # REALLY IMPORTANT TODO
    # TODO
    # SUPER IMPORTANT ***************
    # team = ....


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
    
    
    # pub_date = models.DateTimeField('date published')


class VisualArtsMiddle(Shared):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    TLA = "M.VA"


class VisualArtsElem(Shared):
    artistic_artsyness = models.IntegerField(
        choices=labeledRangeTuple(),
        help_text="Are they artsy? OR Fartsy?")
    TLA = "E.VA"


# TODO: is there a spont middle and a spont elem rubric?
# TODO: This might need to inherit from `Shared`, that is `class Spont(Shared)`
class Spont():
    TLA = "depends_if_there_is_mid_elem"
    pass


# TODO: this needs the rest
ALL_EXCEPT_SPONT = [EngMiddle, VisualArtsMiddle, VisualArtsElem]

# TODO: add spont if it ends up being useful
ALL_COMPETS = ALL_EXCEPT_SPONT  #  + [Spont]
