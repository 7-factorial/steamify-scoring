from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from typing import List, Type, Iterable
from django.utils import timezone

# Create your models here.
from django.urls import reverse
import attr


@attr.s
class AvgAndCount:
    avg = attr.ib()  # type: float
    count = attr.ib()  # type: int


# def rangeTuple(start, endInclusive):
#     return [(x, str(x)) for x in range(start, endInclusive + 1)]

def mean(lis):
    # type: (Iterable[float]) -> float
    al = list(lis)
    return sum(al) / len(al)


def labeledRangeTuple():
    return [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]



def prependstuff(stuff):
    return "</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p>{}".format(stuff)


def htmlListify(rawstr):
    # type: (str) -> str
    spl = rawstr.splitlines()
    stripped = [x.strip() for x in spl]
    noEmpties = [x for x in stripped if x]
    with_lis = "\n".join(format_html("<li>{}</li>", x) for x in noEmpties)
    return "<ul>{}</ul>".format(with_lis)


def standardSteamifyField(help_text_unproc, verbose_name=None, help_text_proc_func=htmlListify):
    return models.IntegerField(
        choices=labeledRangeTuple(),
        help_text=prependstuff(help_text_proc_func(help_text_unproc)),
        verbose_name=verbose_name)
    

    

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


class AllowedDevice(models.Model):

    # possibility for multiple allowed devices 
    judge = models.ForeignKey(
                get_user_model(),
                on_delete=models.PROTECT)
    id = models.CharField(max_length=100, primary_key=True)


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

    def get_attached_Shared_type(self):
        # type: (...) -> Type[Shared]
        from .utils.misc import tla_from_fullId
        team_tla = tla_from_fullId(self.dotted_id)
        for Compet in ALL_EXCEPT_SPONT:
            if Compet.TLA.upper() == team_tla.upper():
                return Compet
        raise ValueError("Could not find a competition for that TeamID.")


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
    # status_for_admin = models.CharField(max_length=200,
    #             blank=True,
    #             choices=[("", ""), 
    #                      ("checked", "checked"),
    #                      ("todo", "todo"),
    #                      ("probably_should_delete", "probably_should_delete"),
    #                      ("probably_should_supersede_older_entry", "probably_should_supersede_older_entry") 
    #                      ])

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
        # type: (Shared) -> str
        from .utils.misc import makeEditLink  # avoid circular import
        return makeEditLink(self.TLA, {
            'spontOrLong': self.spontOrLong,
            'full_team_id': self.team.dotted_id,
            'pk': self.pk})
    
    def avg_judge_submission(self):
        # type: (Shared) -> Averagable
        from .utils.misc import getUserDisplayedAttrs  # avoid circular import
        fns = getUserDisplayedAttrs(self)
        return Averagable([getattr(self, fn) for fn in fns])  # AvgAndCount(avg=mean(vals), count=len(vals))

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
        """,
        verbose_name="Engineering Design/Prototype/Working Model")
        
    engineering_statement = standardSteamifyField("""
        Written statement submitted at the time of performance.
        Statement is neat and has 1-3 spelling/grammatical/punctuation errors.
        Statement links standards to key elements and outcome, but may be unclear in one or two places.
        """)
    

class EngElem(Shared):
    TLA = "E.EN"
    
    presentation = standardSteamifyField("""
        Presentation demonstrates understanding of the material.
        Presenters facilitate engaging discussion regarding challenge expectations 
        Presenters explain their research concerning the shoe  as it relates to environmental sustainability.
        The  purpose of the design is clear, realistic, and share how production may be scaled up.
        Most students have an explicit part in either the explanation or demonstration of the design process regarding the prototype ; however, one or two may function as support.
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    engineering_design_prototype_working_model = standardSteamifyField(""" 
        The operation and design of the prototype somewhat fulfill the challenge, but is unclear in some aspects.
        """,
        verbose_name="Engineering Design/Prototype/Working Model")
        
    engineering_statement = standardSteamifyField("""
        Written statement submitted at the time of performance.
        Statement is neat and has 1-3 spelling/grammatical/punctuation errors.
        Statement links standards to key elements and outcome, but may be unclear in one or two places.
        """)



class VisualArtsMiddle(Shared):
    TLA = "M.VA"
    
    presentation = standardSteamifyField("""
        Presentation clarity (Clear message, some eye contact, appropriate responses, and a suitable presentation standard).
        Some research is observable during the presentation. 
        All but one team member are present OR all are present and one member does not participate.
		""")
        
    artwork = standardSteamifyField("""
        Artwork identifies obvious technology impacts for each year. 
        Artwork illustrates some contrived positive and negative impacts.
        Artwork reflects thorough examination of the topic.
        Artwork develops visual imagery.
        Artwork demonstrates unity of thought, imagery, form, media and techniques in support of creative intent.
		""")
        
    design_notebook = standardSteamifyField(""" 
		Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
		""")
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
		""")


class VisualArtsElem(Shared):
    TLA = "E.VA"
    
    presentation = standardSteamifyField("""
        Presentation clarity (Clear message, some eye contact, appropriate responses, and a suitable presentation standard).
        Some research is observable during the presentation. 
        All but one team member are present OR all are present and one member does not participate.
        """)
        
    artwork = standardSteamifyField("""
        Artwork identifies one technology impact. 
        Artwork illustrates some contrived positive and negative impacts.
        Artwork reflects thorough examination of the topic.
        Artwork develops visual imagery.
        Artwork demonstrates unity of thought, imagery, form, media and techniques in support of creative intent.
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)



class AeroMiddle(Shared):
    TLA = "M.AE"

    presentation = standardSteamifyField("""
        The machine may be slightly damaged upon landing.
        The machine launches as one complete unit.
        The design includes aesthetic improvements, however some may be distracting or random.
        Most students have an explicit part in either the launching or explanation of the design process; however, one or two may function as support.
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
		""")
        
    fulfillment_of_problem = standardSteamifyField("""
        The execution of the launching and the design of the rocket fulfill all but 1 challenge requirement.
        The flight time is in the middle third of all teams.
		""",
        verbose_name="Fulfillment of Problem")
        
    engineering_statement = standardSteamifyField("""
        Written statement submitted at the time of performance.
        Statement is neat and has 1-3 spelling/grammatical/punctuation errors.
        Statement links standards to key elements and outcome, but may be unclear in one or two places.
		""")



class DanceMiddle(Shared):
    TLA = "M.DA"

    presentation = standardSteamifyField("""
        Storyline or concept of dance incorporates a technological advancement but makes an unclear statement about its effects.
        Music or props, rather than dance elements, tell a majority of the story.
        One prop/costume/set item is not made by students.
		""")
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
		""")


class DanceElem(Shared):
    TLA = "E.DA"

    presentation = standardSteamifyField("""
        Storyline or concept of dance incorporates a technological advancement but makes an unclear statement about its effects.
        Music or props, rather than dance elements, tell a majority of the story.
        One prop/costume/set item is not made by students.
		""")
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)



class DebateMiddle(Shared):
    TLA = "M.DE"

    respect_for_other_team = standardSteamifyField("""
        Most statements and responses were respectful and in appropriate language, but there was one sarcastic remark
        """)
        
    information = standardSteamifyField("""
        Most information presented in the debate was clear and accurate, but was not usually thorough
        """)
        
    rebutal = standardSteamifyField("""
        Most counter-arguments were accurate and relevant, but several were weak.
        """)

    use_of_facts_statistics = standardSteamifyField("""
        Every major point was supported with facts, statistics and/or examples, but the relevance of some was questionable.
        """,
        verbose_name="Use of Facts/Statistics")

    organization = standardSteamifyField("""
        Most counter-arguments were accurate and relevant, but several were weak.
        """)
        
    understanding_of_topic = standardSteamifyField("""
        The team seemed to understand the main points of the topic and presented those with ease.       
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)



class RocketMiddle(Shared):
    TLA = "M.RO"

    presentation = standardSteamifyField("""
        The vehicle includes propulsion, payload and recovery systems.
        The bottom bottle is not damaged in any way.
        The fins are not lower than where the bottle begins.
        The rocket launches as one complete unit.
        The rocket flies mostly straight
        One aesthetic aspect of the rocket does not function to aid the launch.
        The payload is delivered with superficial damage.
        Most students have an explicit part in either the launching or explanation of the design process; however, one or two may function as support.
        """)
        
    engineering_statement = standardSteamifyField("""
        Written statement submitted at the time of performance.
        Statement is neat and has 1-3 spelling/grammatical/punctuation errors.
        Statement links standards to key elements and outcome, but may be unclear in one or two places.
        """)
        
    fulfillment_of_problem = standardSteamifyField("""
        The execution of the launching and the design of the rocket fulfill all but 1 challenge requirement.
        The distance from the middle of the payload’s final destination to the middle of the target is greater than 60.96cm but less than 120 cm.
        """,
        verbose_name="Fulfillment of Problem")
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)




class SpokenMiddle(Shared):
    TLA = "M.SW"

    presentation = standardSteamifyField("""
        All team members have explicit roles in the performance, but one or more have notably lesser roles. 
        Eye contact is made and maintained with the audience with some breaks in the performance. 
        No reading of notes. 
        Verbal cues such as tone, pace, volume and intended pauses are used and further the impact; most are effective.
        Non verbal cues such as gestures, facial expressions and body language are used and further the impact but some may be ineffective.
        Speakers exude positive energy and use animated speech. 
        The performance somewhat fulfills the challenge, but is unclear in some aspects. 
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)
        
    poem = standardSteamifyField("""
        Poem includes language that promotes vivid images that contribute to the poem
        The poem does address the issue at hand.
        The poem has less than 2  grammatical errors.
        The poem is somewhat impactful piece.
        """)

class SpokenElem(Shared):
    TLA = "E.SW"

    presentation = standardSteamifyField("""
        All team members have explicit roles in the performance, but one or more have notably lesser roles. 
        Eye contact is made and maintained with the audience with some breaks in the performance. 
        No reading of notes. 
        Verbal cues such as tone, pace, volume and intended pauses are used and further the impact, but some may be ineffective.
        Non verbal cues such as gestures, facial expressions and body language are used and further the impact but some may be ineffective.
        Speakers exude positive energy and use animated speech. 
        The performance somewhat fulfills the challenge, but is unclear in some aspects. 
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)
        
    poem = standardSteamifyField("""
        Poem includes language that promotes vivid images that contribute to the poem
        The poem does address the issue at hand.
        The poem has less than 2 grammatical errors.
        The poem is somewhat impactful piece.
        """)




class TheaterMiddle(Shared):
    TLA = "M.TH"

    presentation = standardSteamifyField("""
        One prop/costume/set item is not originally made by students.
        Presentation easily heard or understood by audience.
        Presentation mostly fulfills the challenge.
        Time limit exceeded by > 30 s.
        Most students maintained character throughout the play, even when not speaking.  
        Most students have an explicit part in the acting and support.
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)

class TheaterElem(Shared):
    TLA = "E.TH"

    presentation = standardSteamifyField("""
        One prop/costume/set item is not originally made by students.
        Presentation easily heard or understood by audience.
        Presentation mostly fulfills the challenge.
        Time limit exceeded by > 30 s.
        Most students maintained character throughout the play, even when not speaking.  
        Most students have an explicit part in the acting and support.
        """)
        
    design_notebook = standardSteamifyField("""
        Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.
        Design process somewhat chronicled.
        Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).
        """)
        
    artist_statement = standardSteamifyField("""
        Statement is neat and has less than two spelling/grammatical/punctuation errors.
        Statement includes standards and key elements 
        How some standards/elements fit into story outcome is somewhat unclear.
        Statement includes description of team work, but each member’s role is not clear.
        """)

_identFunc = lambda x: x

class Spont(Shared):
    TLA = "FAKE_TLA_FOR_SPONT"
    # # There shouldn't be a TLA for Spont because all teams have another category; 
    #  BUT TODO: I need to check where TLA is used to make sure I don't assume 1-to-1 
    # and therefore break Spont
    # # TODO add rubric
    spontOrLong = "spont"
    focus_on_the_task = standardSteamifyField("""
        <ul>
            <li>Almost all team members (one person did not fulfill one of the following):
                <ul>
                    <li>Stay on task all of the time without reminders.</li>
                    <li>Work hard and helps others in the group.</li>
                    <li>Gather information and shares useful ideas for discussions.</li>
                </ul>
            </li>
        </ul>""",
        help_text_proc_func=_identFunc)
    
    listening_questioning_discussing = standardSteamifyField("""
        Respectfully listens, discusses and asks questions.""",
        verbose_name="Listening, questioning, discussing")
    
    teamwork = standardSteamifyField("""
        <ul><li>Almost all team members (one person did not fulfill one of the following):
            <ul>
                <li>Contributed equally to the finished project.</li>
                <li>Worked until the end of the task.</li>
                <li>Actively seek and suggest solutions to problems.</li>
            </ul>
        </li></ul>
        """,
        help_text_proc_func=_identFunc)

    success_in_problem_resolution = standardSteamifyField("""The problem was almost resolved.""")



# VERIFIED 2019 Oct 7 at 5:02 pm - this contains all competitions
ALL_EXCEPT_SPONT = [EngMiddle, EngElem, VisualArtsMiddle, VisualArtsElem,
                    AeroMiddle, DanceMiddle, DanceElem, DebateMiddle, 
                    RocketMiddle, SpokenMiddle, SpokenElem, TheaterMiddle,
                    TheaterElem]  # type: List[Type[Shared]]

# TODO: add spont if it ends up being useful
ALL_COMPETS = ALL_EXCEPT_SPONT + [Spont]
