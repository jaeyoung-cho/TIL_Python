# Generated by Django 2.1 on 2018-11-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_model', '0002_person_try_to_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('try_to_travel', models.BooleanField()),
            ],
        ),
    ]