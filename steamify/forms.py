from django import forms
from .models import Team


class PickTeamIdForm(forms.Form):
    full_team_id = forms.CharField()

    def clean_full_team_id(self):
        # type: (...) -> str
        ftid = self.cleaned_data['full_team_id'].upper()  # type: str

        if not Team.objects.filter(dotted_id=ftid).exists():  # pylint: disable=no-member
            raise forms.ValidationError("Error: did not recognize the team id '{}'. Try again.".format(ftid))

        # Django docs say:
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return ftid
