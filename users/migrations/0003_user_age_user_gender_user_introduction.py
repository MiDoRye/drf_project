# Generated by Django 4.2 on 2023-04-28 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_date_of_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "male"), ("F", "female")], max_length=1
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="introduction",
            field=models.TextField(null=True),
        ),
    ]
