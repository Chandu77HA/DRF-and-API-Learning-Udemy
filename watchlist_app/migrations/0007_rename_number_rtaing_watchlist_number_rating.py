# Generated by Django 4.2.3 on 2023-08-06 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_watchlist_avg_rating_watchlist_number_rtaing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='number_rtaing',
            new_name='number_rating',
        ),
    ]