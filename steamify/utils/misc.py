from django.urls import reverse
from typing import Dict, Any, Type, Union, Set, List, Iterable, cast
from ..models import Shared, EngMiddle
from .faketypes import ModelField


shared_fields_to_exlude_in_user_forms = ["judge", "team", "created_at", "modified_at", "status_for_admin"]

_expanded_excluded = ["id", "shared_ptr"] + shared_fields_to_exlude_in_user_forms


def getUserDisplayedFields(instanceOrClass):
    # type: (Union[Type[Shared], Shared]) -> List[ModelField]
    
    exlu = set(_expanded_excluded)

    def _want(f):
        # type: (ModelField) -> bool
        return f.name not in exlu

    fds = instanceOrClass._meta.get_fields(include_parents=False)  
    castfds = cast(Iterable[ModelField], fds)
    return list(filter(_want, castfds))


def getUserDisplayedAttrs(instanceOrClass):
    # type: (Union[Type[Shared], Shared]) -> List[str]
    fds = getUserDisplayedFields(instanceOrClass)
    return [x.name for x in fds]
    
    # these are filtered earlier now.
    # return names - {"id", "shared_ptr"} - set(shared_fields_to_exlude_in_user_forms)

    # the next two commented lines are from an older attempt.
    # widgets = dict((nam, RadioSelect) for nam in namesForDict)  # type: Dict[str, Input]
    # return widgets

assert getUserDisplayedAttrs(EngMiddle) == ["presentation", "design_notebook", "engineering_design_prototype_working_model", "engineering_statement"]
# TODO: a test for spont

def score_instance_to_dict(instance):
    # type: (Shared) -> Dict[str, str]
    """Like django's model_to_dict, but using pretty names.
    Excludes fields that aren't relevant to the users (judges)."""

    fds = getUserDisplayedFields(instance)
    # source in case I want to double check: https://stackoverflow.com/questions/51905712/how-to-get-the-value-of-a-django-model-field-object
    return dict((f.verbose_name, getattr(instance, f.name)) for f in fds)


def makeEditLink(tla, revkwargs):
    # type: (str, dict) -> str
    if tla == "FAKE_TLA_FOR_SPONT":
        partial = "spont"
    else:
        partial = tla
    editname = 'steamify:{}-edit'.format(partial)
    return reverse(editname, kwargs=revkwargs)
