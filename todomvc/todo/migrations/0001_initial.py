# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('completed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
    ]
