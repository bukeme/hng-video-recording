# Generated by Django 3.2.2 on 2023-10-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='transcription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
