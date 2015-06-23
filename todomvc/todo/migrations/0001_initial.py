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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
    ]
