from django.contrib import admin

# Register your models here.

from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)

# Not sure if we'll use this approach.
# from .models import EngMiddle, Shared, VisualArtsMiddle

# admin.site.register(EngMiddle)
# admin.site.register(VisualArtsMiddle)
