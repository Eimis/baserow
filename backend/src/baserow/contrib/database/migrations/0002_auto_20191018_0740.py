# Generated by Django 2.2.2 on 2019-10-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='group',
            new_name='database',
        ),
        migrations.AddField(
            model_name='table',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]