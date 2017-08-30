# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_sekolah', '0002_remove_agama_aktif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, verbose_name='Nama Jurusan')),
            ],
            options={
                'db_table': 'jurusan',
                'verbose_name_plural': 'Jurusan',
            },
        ),
        migrations.CreateModel(
            name='siswa',
            fields=[
                ('no_induk', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='No Induk Siswa')),
                ('nama', models.CharField(max_length=100, verbose_name='Nami')),
                ('ttl', models.DateField(help_text='Format Tanggal: YYYY-MM-DD', verbose_name='Tanggal Lahir')),
                ('jk', models.CharField(choices=[('laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], default='laki', max_length=15, verbose_name='Jenis Kelamin')),
                ('nama_ortu', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_sekolah.Agama', verbose_name='Agama')),
            ],
            options={
                'db_table': 'siswa',
                'verbose_name_plural': 'Siswa',
            },
        ),
    ]
