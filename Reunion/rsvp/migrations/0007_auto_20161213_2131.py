# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_auto_20161213_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='member',
            field=models.CharField(choices=[(b'onesta', b'Onesta'), (b'cecilia', b'Cecilia'), (b'priscilla', b'Priscilla'), (b'lily', b'Lily Mae'), (b'curly', b'Curly'), (b'ophelia', b'Ophelia'), (b'abby', b'Abby')], max_length=50),
        ),
    ]
