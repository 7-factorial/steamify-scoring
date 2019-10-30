from ..models import Team, Shared, mean
from enum import Enum
from typing import List, Dict, Tuple, Iterable
from .misc import score_instance_to_dict



class LS(Enum):
    LONG = "Long Problem"
    SPONT = "Spontaneous"
   

def getSubmissions(team, ls):
    # type: (Team, LS) -> List[Shared]
    Compet = team.get_attached_Shared_type()
    return list(Compet.objects.filter(team=team))


def averageByKey(scoreDicts):
    # type: (List[Dict[str, int]]) -> Dict[str, float]

    def _avgOneKey(key):
        # type: (str) -> Tuple[str, float]
        return key, mean(x[key] for x in scoreDicts)

    if len(scoreDicts) == 0:  # special case
        keys = []  # type: Iterable[str]
    else:
        keys = scoreDicts[0].keys()
    return dict(map(_avgOneKey, keys))


def getAverages(submissions):
    # type: (List[Shared]) -> Dict[str, float]
    scoreDicts = list(map(score_instance_to_dict, submissions))  # type: List[Dict[str, int]]
    return averageByKey(scoreDicts)  


def getLongOrSpont(team, ls):
    # type: (Team, LS) -> dict

    submissions = getSubmissions(team, ls)
    numjudges = len(submissions) 

    return {
        "ls": ls,
        "numjudges": numjudges,
        "categs": getAverages(submissions)
    }
    

def makeTeamScoreData(team):
    # type: (Team) -> dict
    return {
        "team": team,
        "long": getLongOrSpont(team, LS.LONG),
        "spont": getLongOrSpont(team, LS.SPONT),
    }