# Generated by Django 5.1.5 on 2025-01-28 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1970)]),
        ),
    ]
