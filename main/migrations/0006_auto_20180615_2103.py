# Generated by Django 2.0.4 on 2018-06-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180615_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='penguin',
            options={'permissions': (('can_see_penguins', 'can_play_with_penguines'),)},
        ),
    ]