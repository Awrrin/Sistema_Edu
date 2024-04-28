# Generated by Django 4.2.11 on 2024-04-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pedidos",
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
                ("title", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateField(null=True)),
                ("obser", models.CharField(max_length=300, null=True)),
                ("finished_at", models.DateTimeField(null=True)),
            ],
        ),
    ]
