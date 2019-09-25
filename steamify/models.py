from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.urls import reverse



def rangeTuple(start, endInclusive):
    return [(x, str(x)) for x in range(start, endInclusive + 1)]


class Team(models.Model):
    dotted_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return "'{}' ({})".format(self.name, self.dotted_id)




class Shared(models.Model):
    something_shared = models.IntegerField(
        choices=rangeTuple(1, 5),
        help_text="Did they do somethign well that involes all competitions?")
    judge = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        )
    # REALLY IMPORTANT TODO
    # TODO
    # SUPER IMPORTANT ***************
    # team = ....

    def save(self, *args, **kwargs):
        if self._state.adding:
            print("ADDING\n"*5)
        else:
            print("NOT ADDING\n"*5)
        # self.judge = 
        super().save(*args, **kwargs)  # Call the "real" save() method.

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
# TODO: This might need to inherit from `Shared`, that is `class Spont(Shared)`
class Spont():
    TLA = "depends_if_there_is_mid_elem"
    pass


# TODO: this needs the rest
ALL_EXCEPT_SPONT = [EngMiddle, VisualArtsMiddle, VisualArtsElem]

# TODO: add spont if it ends up being useful
ALL_COMPETS = ALL_EXCEPT_SPONT  #  + [Spont]
