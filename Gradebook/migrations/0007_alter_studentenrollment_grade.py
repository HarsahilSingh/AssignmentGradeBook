# Generated by Django 4.0.4 on 2022-06-08 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gradebook', '0006_alter_semester_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrollment',
            name='grade',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
