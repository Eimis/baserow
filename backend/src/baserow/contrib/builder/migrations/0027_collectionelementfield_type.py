# Generated by Django 3.2.21 on 2023-10-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0026_element_styling_properties"),
    ]

    operations = [
        migrations.AddField(
            model_name="collectionelementfield",
            name="type",
            field=models.CharField(
                default="text", help_text="The type of the field.", max_length=225
            ),
        ),
        migrations.RenameModel(
            old_name="CollectionElementField",
            new_name="CollectionField",
        ),
    ]
