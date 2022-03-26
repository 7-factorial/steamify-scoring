from django.core.management.base import BaseCommand
from steamify.models import Team, ALL_COMPETS, Shared
from django.contrib.auth.models import User



class Command(BaseCommand):

    def handle(self, *args, **options):    
        ## commented for safety

        # print("Deleting the following:")
        # print(" - all score submissions")
        # for Compet in ALL_COMPETS:
            # Compet.objects.all().delete()

        # print(" - all Teams")
        # Team.objects.all().delete()

        # print(" - all Users (except 'staff'")
        # User.objects.filter(is_staff=False).delete()

        # shareds = list(Shared.objects.all())
        # if shareds:
        #     raise ValueError("There shouldn't be 'shareds' at this point.")
        #     print(shareds)
        #     Shared.objects.all().delete()
        
        pass
