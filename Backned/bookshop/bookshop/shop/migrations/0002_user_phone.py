# Generated by Django 5.0.6 on 2024-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]