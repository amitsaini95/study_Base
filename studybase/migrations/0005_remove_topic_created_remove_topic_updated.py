# Generated by Django 5.0.1 on 2024-02-21 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studybase', '0004_alter_topic_created_alter_topic_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='created',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='updated',
        ),
    ]
