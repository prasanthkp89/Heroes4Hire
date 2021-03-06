# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=20)),
                ('typeofClass', models.CharField(choices=[(b'AC', b'Armed Combat'), (b'UC', b'Unarmed Combat'), (b'P', b'Piloting'), (b'O', b'Other')], max_length=5)),
                ('description', models.TextField(default=b'Please Add Description')),
            ],
        ),
        migrations.CreateModel(
            name='ReportLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=5)),
                ('outcome', models.CharField(choices=[(b'P', b'Pass'), (b'F', b'Fail')], max_length=1)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=15)),
                ('address', models.TextField(default=b'Please Add Address')),
                ('citizenship', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='reportlog',
            name='TrainerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Trainer'),
        ),
        migrations.AddField(
            model_name='reportlog',
            name='classID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.ClassTraining'),
        ),
        migrations.AddField(
            model_name='reportlog',
            name='heroID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heroes.Hero'),
        ),
        migrations.AddField(
            model_name='classtraining',
            name='TrainerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Trainer'),
        ),
        migrations.AddField(
            model_name='classtraining',
            name='roomID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Room'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='classID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.ClassTraining'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='heroID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heroes.Hero'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='roomID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Room'),
        ),
    ]
