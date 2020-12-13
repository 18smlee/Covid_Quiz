# Generated by Django 3.1.3 on 2020-12-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0004_quizuser_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ManyToManyField(to='quizApp.quizUser'),
        ),
    ]
