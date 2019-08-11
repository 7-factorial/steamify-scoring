listOfScoresFromDifferentJudges = Scores.objects.filter(team_id="E.VA.123", competition_type="spont")
mean(listOfScoresFromDifferentJudges)