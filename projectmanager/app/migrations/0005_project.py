# Generated by Django 3.1.1 on 2020-10-26 07:28

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_team_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synopsis', tinymce.models.HTMLField()),
                ('phase1', tinymce.models.HTMLField()),
                ('phase2', tinymce.models.HTMLField()),
                ('fianle', tinymce.models.HTMLField()),
                ('project_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.team')),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
