# Generated by Django 4.1.7 on 2023-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITERECRESTAU', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.CharField(max_length=10000),
        ),
    ]
