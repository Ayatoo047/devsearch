# Generated by Django 4.0.5 on 2022-09-29 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
