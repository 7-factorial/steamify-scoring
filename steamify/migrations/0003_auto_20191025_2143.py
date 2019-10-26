# Generated by Django 2.2.4 on 2019-10-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamify', '0002_auto_20191022_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeromiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='aeromiddle',
            name='engineering_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Written statement submitted at the time of performance.</li>\n<li>Statement is neat and has 1-3 spelling/grammatical/punctuation errors.</li>\n<li>Statement links standards to key elements and outcome, but may be unclear in one or two places.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='aeromiddle',
            name='fulfillment_of_problem',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The execution of the launching and the design of the rocket fulfill all but 1 challenge requirement.</li>\n<li>The flight time is in the middle third of all teams.</li></ul>", verbose_name='Fulfillment of Problem'),
        ),
        migrations.AlterField(
            model_name='aeromiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The machine may be slightly damaged upon landing.</li>\n<li>The machine launches as one complete unit.</li>\n<li>The design includes aesthetic improvements, however some may be distracting or random.</li>\n<li>Most students have an explicit part in either the launching or explanation of the design process; however, one or two may function as support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='danceelem',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='danceelem',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='danceelem',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Storyline or concept of dance incorporates a technological advancement but makes an unclear statement about its effects.</li>\n<li>Music or props, rather than dance elements, tell a majority of the story.</li>\n<li>One prop/costume/set item is not made by students.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='dancemiddle',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='dancemiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='dancemiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Storyline or concept of dance incorporates a technological advancement but makes an unclear statement about its effects.</li>\n<li>Music or props, rather than dance elements, tell a majority of the story.</li>\n<li>One prop/costume/set item is not made by students.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='information',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Most information presented in the debate was clear and accurate, but was not usually thorough</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='organization',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Most counter-arguments were accurate and relevant, but several were weak.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='rebutal',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Most counter-arguments were accurate and relevant, but several were weak.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='respect_for_other_team',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Most statements and responses were respectful and in appropriate language, but there was one sarcastic remark</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='understanding_of_topic',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The team seemed to understand the main points of the topic and presented those with ease.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='debatemiddle',
            name='use_of_facts_statistics',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Every major point was supported with facts, statistics and/or examples, but the relevance of some was questionable.</li></ul>", verbose_name='Use of Facts/Statistics'),
        ),
        migrations.AlterField(
            model_name='engelem',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='engelem',
            name='engineering_design_prototype_working_model',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The operation and design of the prototype somewhat fulfill the challenge, but is unclear in some aspects.</li></ul>", verbose_name='Engineering Design/Prototype/Working Model'),
        ),
        migrations.AlterField(
            model_name='engelem',
            name='engineering_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Written statement submitted at the time of performance.</li>\n<li>Statement is neat and has 1-3 spelling/grammatical/punctuation errors.</li>\n<li>Statement links standards to key elements and outcome, but may be unclear in one or two places.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='engelem',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Presentation demonstrates understanding of the material.</li>\n<li>Presenters facilitate engaging discussion regarding challenge expectations</li>\n<li>Presenters explain their research concerning the shoe  as it relates to environmental sustainability.</li>\n<li>The  purpose of the design is clear, realistic, and share how production may be scaled up.</li>\n<li>Most students have an explicit part in either the explanation or demonstration of the design process regarding the prototype ; however, one or two may function as support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='engmiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='engmiddle',
            name='engineering_design_prototype_working_model',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The operation and design of the prototype somewhat fulfill the challenge, but is unclear in some aspects.</li></ul>", verbose_name='Engineering Design/Prototype/Working Model'),
        ),
        migrations.AlterField(
            model_name='engmiddle',
            name='engineering_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Written statement submitted at the time of performance.</li>\n<li>Statement is neat and has 1-3 spelling/grammatical/punctuation errors.</li>\n<li>Statement links standards to key elements and outcome, but may be unclear in one or two places.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='engmiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Presentation demonstrates understanding of the material.</li>\n<li>Presenters facilitate engaging discussion regarding challenge expectations.</li>\n<li>Presenters explain their research concerning the CO2 device as it relates to environmental sustainability.</li>\n<li>The purpose of the design is clear, realistic, and presenters share how it may be scaled up.</li>\n<li>Most students have an explicit part in either the explanation or demonstration of the design process regarding the prototype; however, one or two may function as support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='rocketmiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='rocketmiddle',
            name='engineering_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Written statement submitted at the time of performance.</li>\n<li>Statement is neat and has 1-3 spelling/grammatical/punctuation errors.</li>\n<li>Statement links standards to key elements and outcome, but may be unclear in one or two places.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='rocketmiddle',
            name='fulfillment_of_problem',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The execution of the launching and the design of the rocket fulfill all but 1 challenge requirement.</li>\n<li>The distance from the middle of the payload’s final destination to the middle of the target is greater than 60.96cm but less than 120 cm.</li></ul>", verbose_name='Fulfillment of Problem'),
        ),
        migrations.AlterField(
            model_name='rocketmiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The vehicle includes propulsion, payload and recovery systems.</li>\n<li>The bottom bottle is not damaged in any way.</li>\n<li>The fins are not lower than where the bottle begins.</li>\n<li>The rocket launches as one complete unit.</li>\n<li>The rocket flies mostly straight</li>\n<li>One aesthetic aspect of the rocket does not function to aid the launch.</li>\n<li>The payload is delivered with superficial damage.</li>\n<li>Most students have an explicit part in either the launching or explanation of the design process; however, one or two may function as support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenelem',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenelem',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenelem',
            name='poem',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Poem includes language that promotes vivid images that contribute to the poem</li>\n<li>The poem does address the issue at hand.</li>\n<li>The poem has less than 2 grammatical errors.</li>\n<li>The poem is somewhat impactful piece.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenelem',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>All team members have explicit roles in the performance, but one or more have notably lesser roles.</li>\n<li>Eye contact is made and maintained with the audience with some breaks in the performance.</li>\n<li>No reading of notes.</li>\n<li>Verbal cues such as tone, pace, volume and intended pauses are used and further the impact, but some may be ineffective.</li>\n<li>Non verbal cues such as gestures, facial expressions and body language are used and further the impact but some may be ineffective.</li>\n<li>Speakers exude positive energy and use animated speech.</li>\n<li>The performance somewhat fulfills the challenge, but is unclear in some aspects.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenmiddle',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenmiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenmiddle',
            name='poem',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Poem includes language that promotes vivid images that contribute to the poem</li>\n<li>The poem does address the issue at hand.</li>\n<li>The poem has less than 2  grammatical errors.</li>\n<li>The poem is somewhat impactful piece.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spokenmiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>All team members have explicit roles in the performance, but one or more have notably lesser roles.</li>\n<li>Eye contact is made and maintained with the audience with some breaks in the performance.</li>\n<li>No reading of notes.</li>\n<li>Verbal cues such as tone, pace, volume and intended pauses are used and further the impact; most are effective.</li>\n<li>Non verbal cues such as gestures, facial expressions and body language are used and further the impact but some may be ineffective.</li>\n<li>Speakers exude positive energy and use animated speech.</li>\n<li>The performance somewhat fulfills the challenge, but is unclear in some aspects.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spont',
            name='focus_on_the_task',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p>\n        <ul>\n            <li>Almost all team members (one person did not fulfill one of the following):\n                <ul>\n                    <li>Stay on task all of the time without reminders.</li>\n                    <li>Work hard and helps others in the group.</li>\n                    <li>Gather information and shares useful ideas for discussions.</li>\n                </ul>\n            </li>\n        </ul>"),
        ),
        migrations.AlterField(
            model_name='spont',
            name='listening_questioning_discussing',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Respectfully listens, discusses and asks questions.</li></ul>", verbose_name='Listening, questioning, discussing'),
        ),
        migrations.AlterField(
            model_name='spont',
            name='success_in_problem_resolution',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>The problem was almost resolved.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='spont',
            name='teamwork',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p>\n        <ul><li>Almost all team members (one person did not fulfill one of the following):\n            <ul>\n                <li>Contributed equally to the finished project.</li>\n                <li>Worked until the end of the task.</li>\n                <li>Actively seek and suggest solutions to problems.</li>\n            </ul>\n        </li></ul>\n        "),
        ),
        migrations.AlterField(
            model_name='theaterelem',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='theaterelem',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='theaterelem',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>One prop/costume/set item is not originally made by students.</li>\n<li>Presentation easily heard or understood by audience.</li>\n<li>Presentation mostly fulfills the challenge.</li>\n<li>Time limit exceeded by &gt; 30 s.</li>\n<li>Most students maintained character throughout the play, even when not speaking.</li>\n<li>Most students have an explicit part in the acting and support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='theatermiddle',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='theatermiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='theatermiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>One prop/costume/set item is not originally made by students.</li>\n<li>Presentation easily heard or understood by audience.</li>\n<li>Presentation mostly fulfills the challenge.</li>\n<li>Time limit exceeded by &gt; 30 s.</li>\n<li>Most students maintained character throughout the play, even when not speaking.</li>\n<li>Most students have an explicit part in the acting and support.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartselem',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartselem',
            name='artwork',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Artwork identifies one technology impact.</li>\n<li>Artwork illustrates some contrived positive and negative impacts.</li>\n<li>Artwork reflects thorough examination of the topic.</li>\n<li>Artwork develops visual imagery.</li>\n<li>Artwork demonstrates unity of thought, imagery, form, media and techniques in support of creative intent.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartselem',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartselem',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Presentation clarity (Clear message, some eye contact, appropriate responses, and a suitable presentation standard).</li>\n<li>Some research is observable during the presentation.</li>\n<li>All but one team member are present OR all are present and one member does not participate.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartsmiddle',
            name='artist_statement',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Statement is neat and has less than two spelling/grammatical/punctuation errors.</li>\n<li>Statement includes standards and key elements</li>\n<li>How some standards/elements fit into story outcome is somewhat unclear.</li>\n<li>Statement includes description of team work, but each member’s role is not clear.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartsmiddle',
            name='artwork',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Artwork identifies obvious technology impacts for each year.</li>\n<li>Artwork illustrates some contrived positive and negative impacts.</li>\n<li>Artwork reflects thorough examination of the topic.</li>\n<li>Artwork develops visual imagery.</li>\n<li>Artwork demonstrates unity of thought, imagery, form, media and techniques in support of creative intent.</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartsmiddle',
            name='design_notebook',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Relevant research from more than 3 different reputable resources is included and documented in the design notebook in “Resources” section.</li>\n<li>Design process somewhat chronicled.</li>\n<li>Design notebook quality is at standard (Table of contents is inaccurate, page numbers are mostly correct, titles and dates are somewhat clear, entries and figures are clear).</li></ul>"),
        ),
        migrations.AlterField(
            model_name='visualartsmiddle',
            name='presentation',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text="</p><p style='margin-bottom:0px; color:#777;'><em>Example of a score of <b>3</b>:</em></p><ul><li>Presentation clarity (Clear message, some eye contact, appropriate responses, and a suitable presentation standard).</li>\n<li>Some research is observable during the presentation.</li>\n<li>All but one team member are present OR all are present and one member does not participate.</li></ul>"),
        ),
    ]
