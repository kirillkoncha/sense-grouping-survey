# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.FloatField()),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Контекст',
                'verbose_name_plural': 'Контексты',
            },
        ),
        migrations.CreateModel(
            name='ContextGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Группировка контекстов',
                'verbose_name_plural': 'Группировки контекстов',
            },
        ),
        migrations.CreateModel(
            name='ContextSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('order', models.FloatField()),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Набор контекстов для слова',
                'verbose_name_plural': 'Наборы контекстов для слов',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadingHand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profession', models.TextField(verbose_name='Образование')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('sex', models.BooleanField(verbose_name='Пол')),
                ('languages', models.TextField(help_text='пожалуйста, перечислите все', verbose_name='Родной язык/языки')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('feedback', models.TextField(blank=True, default='')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Education', verbose_name='Последняя законченная ступень образования')),
                ('leading_hand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.LeadingHand', verbose_name='Ведущая рука')),
            ],
            options={
                'verbose_name': 'Испытуемый',
                'verbose_name_plural': 'Испытуемые',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contextgroup',
            name='context_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.ContextSet'),
        ),
        migrations.AddField(
            model_name='contextgroup',
            name='contexts',
            field=models.ManyToManyField(to='survey.Context'),
        ),
        migrations.AddField(
            model_name='contextgroup',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Participant'),
        ),
        migrations.AddField(
            model_name='context',
            name='context_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.ContextSet'),
        ),
        migrations.AlterUniqueTogether(
            name='contextgroup',
            unique_together=set([('participant', 'context_set')]),
        ),
    ]
