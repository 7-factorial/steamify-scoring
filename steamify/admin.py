from django.contrib import admin

# Register your models here.


# Not sure if we'll use this approach.
from .models import ALL_COMPETS, Team, AllowedDevice   # , Shared, VisualArtsMiddle

for comp in ALL_COMPETS:
    admin.site.register(comp)
admin.site.register(Team)
admin.site.register(AllowedDevice)

# admin.site.register(VisualArtsMiddle)
