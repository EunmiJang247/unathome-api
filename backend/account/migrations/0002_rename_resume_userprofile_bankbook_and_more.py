# Generated by Django 5.0.4 on 2024-04-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='resume',
            new_name='bankBook',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(null=True),
        ),
    ]
