# Generated by Django 5.1.4 on 2024-12-21 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_country_country_name_en_country_country_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user_name', 'hotel')},
        ),
    ]
