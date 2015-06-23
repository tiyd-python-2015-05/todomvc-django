# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
