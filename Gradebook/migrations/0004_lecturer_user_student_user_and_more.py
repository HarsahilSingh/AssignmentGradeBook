# Generated by Django 4.0.4 on 2022-05-28 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gradebook', '0003_semester_courses_alter_semester_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentenrollment',
            name='gradeTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
