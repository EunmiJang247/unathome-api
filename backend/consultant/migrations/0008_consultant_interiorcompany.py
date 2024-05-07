# Generated by Django 5.0.4 on 2024-05-07 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0007_consultant_status'),
        ('interiorcompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='interiorCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interiorcompany.interiorcompany'),
        ),
    ]