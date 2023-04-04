# Generated by Django 3.2.18 on 2023-03-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0066_rename_track_group_usage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="track_workspace_usage",
            field=models.BooleanField(
                default=False,
                help_text="Runs a job once per day which calculates per workspace row counts and file storage usage, displayed on the admin workspace page.",
            ),
        ),
    ]
