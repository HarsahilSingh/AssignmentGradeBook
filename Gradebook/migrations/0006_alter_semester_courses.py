# Generated by Django 4.0.4 on 2022-06-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gradebook', '0005_alter_class_lecturer_alter_lecturer_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='courses',
            field=models.ManyToManyField(blank=True, to='Gradebook.course'),
        ),
    ]
