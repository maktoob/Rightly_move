# Generated by Django 3.1.5 on 2021-01-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
