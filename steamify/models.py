from django.db import models

# Create your models here.
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class Shared(models.Model):
    something_one = models.CharField(max_length=200)
    # TODO: add judge = foreignKey(User)
    # maybe TODO? add grade_and_category

    # stg_two = models.CharField(max_length=200)

    # YEAR_IN_SCHOOL_CHOICES = [(x, str(x)) for x in range(1, 5+1)]
    # year_in_school = models.IntegerField(choices=YEAR_IN_SCHOOL_CHOICES)


# each instance of this will be a single score submission by one judge
class EngMiddle(Shared):
    presentation_quality = models.CharField(help_text="Did they present well? Did they do the things?", max_length=200)
    # pub_date = models.DateTimeField('date published')

    def get_absolute_url(self):
        return reverse('steamify:engmid-view', kwargs={"pk": self.id})


class VisualArtsMiddle(Shared):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
