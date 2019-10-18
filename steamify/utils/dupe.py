from ..models import Shared, ALL_COMPETS
from typing import Type, Optional, Iterable, Tuple
from django import db


# def getUnblankStatus():
#     # () -> Not_None
    
#     def _one(compet):
#         # type: (db.models.model) -> Tuple[str, list]
#         competData = list(compet.objects.exclude(status_for_admin=""))
#         return compet.__name__, competData

#     # Probably do some more testing on this. Other example code
#     #   is below; not sure if I'll need
#     return dict(map(_one, ALL_COMPETS))
    
    
    
#     # def getPastSubmissionsInAllCompets(judgeInstance, spontOrLong):
#     # # type: (auth.models.User, str) -> Optional[dict]

    
#     # def _all():
#     #     # type: () -> dict
#     #     if spontOrLong == "spont":
#     #         return dict([_one(Spont)])
#     #     else:
            
        
#     # resu = _all()
#     # if not any(resu.values()):
#     #     return None
#     # else:
#     #     return resu



def getEntriesIfAlreadyExist(instance):
    # type: (Shared) -> Iterable[Shared]
    Compet = type(instance)
    # try:
    # TODO: TEST THIS
    return Compet.objects.filter(
        judge=instance.judge,
        team=instance.team,
    )
    # except Compet.DoesNotExist:
    #     return None