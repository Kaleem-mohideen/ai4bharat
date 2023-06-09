# Generated by Django 3.2.3 on 2023-03-20 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TargetLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=200, verbose_name='Target Languages')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('articleTitle', models.CharField(max_length=500)),
                ('target_lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wikiTranslate.targetlang', verbose_name='Target Language')),
            ],
        ),
    ]
