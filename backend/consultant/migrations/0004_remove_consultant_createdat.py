# Generated by Django 5.0.4 on 2024-05-01 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0003_alter_consultant_marketingagree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='createdAt',
        ),
    ]