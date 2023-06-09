# Generated by Django 4.2 on 2023-04-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female")], max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
