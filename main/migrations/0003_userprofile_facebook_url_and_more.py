# Generated by Django 4.2.7 on 2023-11-21 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lesson_poster_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='language_preference',
            field=models.CharField(blank=True, choices=[('en', 'English')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Instructor', 'Instructor'), ('Student', 'Student'), ('Admin', 'Admin')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='theme_preference',
            field=models.CharField(blank=True, choices=[('Dark Mode', 'Dark'), ('light Mode', 'Light'), ('System Default', 'System')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
