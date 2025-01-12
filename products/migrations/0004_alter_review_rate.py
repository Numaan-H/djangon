# Generated by Django 5.1.4 on 2025-01-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_review_ratings_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None),
        ),
    ]
