# Generated by Django 3.0.4 on 2020-03-26 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="budget", old_name="budget", new_name="balance",
        ),
    ]
