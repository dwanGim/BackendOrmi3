# Generated by Django 4.2.5 on 2023-10-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='tube/files/%Y/%m/%d/'),
        ),
    ]
