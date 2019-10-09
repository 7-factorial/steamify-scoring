from django.forms.models import model_to_dict
from django.urls import reverse



def score_instance_to_dict(instance):
    """model_to_dict with appropriate fields excluded."""
    return model_to_dict(instance, exclude=["id", "shared_ptr", "judge", "team", "created_at", "modified_at"])


def makeEditLink(tla, revkwargs):
    # type: (str, dict) -> str
    import pdb; pdb.set_trace()
    editname = 'steamify:{}-edit'.format(tla)
    return reverse(editname, kwargs=revkwargs)
