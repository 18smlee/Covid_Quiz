# Generated by Django 3.1.4 on 2020-12-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0011_remove_response_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='userChoice',
            field=models.IntegerField(choices=[(0, 'Never'), (1, 'Once Pm'), (2, 'Once Pw'), (3, 'Everyday')], default=0),
        ),
    ]