from django.contrib import admin

# Register your models here.


# Not sure if we'll use this approach.
from .models import EngMiddle, Team   # , Shared, VisualArtsMiddle

admin.site.register(EngMiddle)
admin.site.register(Team)

# admin.site.register(VisualArtsMiddle)
