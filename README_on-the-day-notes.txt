
fake team for practice: M.DE.999

https://steamify.pythonanywhere.com/steamify/adminstatus
https://steamify.pythonanywhere.com/steamify/adminjudgelist
https://steamify.pythonanywhere.com/admin

Keep an eye on...
- duplicate submissions (but if not identical, ask)


How to:
- Add a team that wasn't added somehow:
  
    ## in proper venv
    python3 manage.py shell
    from steamify.models import Team
    Team.objects.create(dotted_id="M.EN.998",
                name="Team Name Here",
                school_name="School Name Here")

- Add a judge:
  Just use the graphical add-user interface.