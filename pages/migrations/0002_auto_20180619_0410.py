# Generated by Django 2.0.4 on 2018-06-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagedomains',
            name='audience',
        ),
        migrations.RemoveField(
            model_name='pages',
            name='content',
        ),
        migrations.AddField(
            model_name='pages',
            name='audience',
            field=models.CharField(default='public', max_length=50),
            preserve_default=False,
        ),
    ]
