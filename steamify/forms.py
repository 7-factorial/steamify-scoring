from django import forms
from .models import Team


class PickTeamIdForm(forms.Form):
    full_team_id = forms.CharField()

    def clean_full_team_id(self):
        ftid = self.cleaned_data['full_team_id']

        # Maybe TODO: should the teamnames be in a text file?
        # if ftid not in ["hardcoded", "list", "of", "teams", "which", "definitely", "should", "not", "be", "hardcoded", "E.VA.156", "E.EN.278", "M.RO.390", "M.EN.432"]:
        if not Team.objects.filter(dotted_id=ftid).exists():  # pylint: disable=no-member
            raise forms.ValidationError("Error: did not recognize the team id '{}'. Try again.".format(ftid))

        # Django docs say:
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return ftid
