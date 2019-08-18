listOfScoresFromDifferentJudges = Scores.objects.filter(full_team_id="E.VA.123", competition_type="spont")
mean(listOfScoresFromDifferentJudges)
