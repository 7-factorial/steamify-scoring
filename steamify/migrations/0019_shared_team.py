# Generated by Django 2.2.4 on 2019-10-08 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steamify', '0018_aeromiddle_danceelem_dancemiddle_debatemiddle_engelem_rocketmiddle_spokenelem_spokenmiddle_theaterel'),
    ]

    operations = [
        migrations.AddField(
            model_name='shared',
            name='team',
            field=models.ForeignKey(default='M.EN.358', on_delete=django.db.models.deletion.PROTECT, to='steamify.Team'),
            preserve_default=False,
        ),
    ]