# Generated by Django 5.0.4 on 2024-05-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0002_consultant_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='marketingAgree',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='personalInfoAgree',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='consultantimage',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
