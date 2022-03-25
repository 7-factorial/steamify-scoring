
- Here's my judge canned directions:
   - You can use your cellular data or the on-campus wifi. Cellular data is recommended for reliability.
   - Log in now.
     - What is your name? Username is jwilli (5 letters of last name).
       - Two exceptions: Kat Barker: katbarke; Kim Barker: kimbarke
     - Password is s____________m.
   - Pick Long Problem or Spontaneous appropriately.
   - Try judging the fake team 999 now.
   - Notice that the descriptions are given for a score of **3**.
   - If you have any questions or issues, please ask a board member.



fake team for practice: pick high numbers, or 999

https://steamify.pythonanywhere.com/steamify/adminstatus
https://steamify.pythonanywhere.com/steamify/adminjudgelist
https://steamify.pythonanywhere.com/admin

Keep an eye on...
- duplicate submissions (but if not identical, ask)

- Do periodic downloads of the data to local

How to:
- Add a team that wasn't added somehow:
  
    ## do this in proper venv
    python3 manage.py shell
    from steamify.models import Team
    Team.objects.create(dotted_id="M.EN.998",
                name="Team Name Here",
                school_name="School Name Here")

- Add a judge:
  Just use the graphical add-user interface.
