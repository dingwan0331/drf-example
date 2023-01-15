# Generated by Django 4.1.5 on 2023-01-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("content", models.CharField(max_length=200)),
                ("created", models.DateTimeField()),
            ],
            options={
                "db_table": "comments",
            },
        ),
    ]