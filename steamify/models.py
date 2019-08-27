from django.db import models

# Create your models here.
from django.urls import reverse


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


def rangeTuple(start, endInclusive):
    return [(x, str(x)) for x in range(start, endInclusive + 1)]



class Shared(models.Model):
    something_shared = models.IntegerField(
        choices=rangeTuple(1, 5),
        help_text="Did they do somethign well that involes all competitions?")
    # TODO: add judge = foreignKey(User)
    # maybe TODO? add grade_and_category

    # stg_two = models.CharField(max_length=200)

    # YEAR_IN_SCHOOL_CHOICES = [(x, str(x)) for x in range(1, 5+1)]
    # year_in_school = models.IntegerField(choices=YEAR_IN_SCHOOL_CHOICES)



# each instance of this will be a single score submission by one judge
class EngMiddle(Shared):
    presentation_quality = models.IntegerField(
        choices=rangeTuple(1, 5),
        help_text="Did they present well? Did they do the things?")
    TLA = "M.EN"
    # pub_date = models.DateTimeField('date published')


class VisualArtsMiddle(Shared):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    TLA = "M.VA"


class VisualArtsElem(Shared):
    artistic_artsyness = models.IntegerField(
        choices=rangeTuple(1, 5),
        help_text="Are they artsy? OR Fartsy?")
    TLA = "E.VA"


# TODO: is there a spont middle and a spont elem rubric?
class Spont():
    TLA = "depends_if_there_is_mid_elem"
    pass


# TODO: this needs the rest
ALL_EXCEPT_SPONT = [EngMiddle, VisualArtsMiddle, VisualArtsElem]

# TODO: add spont if it ends up being useful
ALL_COMPETS = ALL_EXCEPT_SPONT  #  + [Spont]
