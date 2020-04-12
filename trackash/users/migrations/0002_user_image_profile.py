# Generated by Django 3.0.4 on 2020-04-12 02:00

from django.db import migrations, models
import trackash.users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image_profile",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=trackash.users.models.user_directory_path,
                verbose_name="Image Profile",
            ),
        ),
    ]