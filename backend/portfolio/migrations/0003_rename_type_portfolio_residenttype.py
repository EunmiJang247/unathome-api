# Generated by Django 5.0.4 on 2024-04-22 14:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_alter_portfolio_onads"),
    ]

    operations = [
        migrations.RenameField(
            model_name="portfolio",
            old_name="type",
            new_name="residentType",
        ),
    ]
