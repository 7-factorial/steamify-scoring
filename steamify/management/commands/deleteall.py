from django.core.management.base import BaseCommand
from steamify.models import Team, ALL_COMPETS, Shared
from django.contrib.auth.models import User



class Command(BaseCommand):

    def handle(self, *args, **options):    
        ## commented for safety

        # for Compet in ALL_COMPETS:
            # Compet.objects.all().delete()

        # Team.objects.all().delete()

        # User.objects.filter(is_staff=False).delete()

        # AllowedDevice.objects.all().delete()

        # shareds = list(Shared.objects.all())
        # if shareds:
        #     print(shareds)
        #     Shared.objects.all().delete()
        
        pass
