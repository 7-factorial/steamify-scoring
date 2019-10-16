from django.forms.models import model_to_dict
from django.urls import reverse



shared_fields_to_exlude_in_user_forms = ["judge", "team", "created_at", "modified_at"]

_expanded_excluded = ["id", "shared_ptr"] + shared_fields_to_exlude_in_user_forms

def score_instance_to_dict(instance):
    """model_to_dict with appropriate fields excluded."""
    return model_to_dict(instance, exclude=_expanded_excluded)


def makeEditLink(tla, revkwargs):
    # type: (str, dict) -> str
    if tla == "FAKE_TLA_FOR_SPONT":
        partial = "spont"
    else:
        partial = tla
    editname = 'steamify:{}-edit'.format(partial)
    return reverse(editname, kwargs=revkwargs)
