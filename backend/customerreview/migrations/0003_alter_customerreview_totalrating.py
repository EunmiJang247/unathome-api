# Generated by Django 5.0.4 on 2024-05-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerreview', '0002_customerreview_intimacyrating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='totalRating',
            field=models.CharField(choices=[('아쉬워요', '아쉬워요'), ('보통이에요', '보통이에요'), ('최고에요', '최고에요')], max_length=20, null=True),
        ),
    ]