# Generated by Django 4.0.1 on 2022-04-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('deptt', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
    ]
