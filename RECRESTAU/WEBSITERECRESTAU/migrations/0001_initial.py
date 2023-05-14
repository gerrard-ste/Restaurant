# Generated by Django 4.1.7 on 2023-05-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('ville', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='restaurant_images/')),
            ],
        ),
    ]
