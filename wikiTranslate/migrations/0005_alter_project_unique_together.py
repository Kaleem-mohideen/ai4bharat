# Generated by Django 4.1.7 on 2023-03-30 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiTranslate', '0004_alter_project_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set(),
        ),
    ]
