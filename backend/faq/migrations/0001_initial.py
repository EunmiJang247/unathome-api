# Generated by Django 5.0.4 on 2024-05-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('contents', models.TextField(null=True)),
            ],
        ),
    ]