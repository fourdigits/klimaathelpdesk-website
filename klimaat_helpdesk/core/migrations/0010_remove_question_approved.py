# Generated by Django 3.1.2 on 2021-03-27 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_question_original_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='approved',
        ),
    ]
