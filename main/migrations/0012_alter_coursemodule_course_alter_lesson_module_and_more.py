# Generated by Django 4.2.7 on 2023-11-28 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='course',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='main.coursemodule'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='poster_url',
            field=models.FileField(upload_to='posters/'),
        ),
    ]
