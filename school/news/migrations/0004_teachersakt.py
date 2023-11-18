# Generated by Django 3.2.16 on 2023-06-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20221226_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersAkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Имя')),
                ('name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('email', models.CharField(max_length=500, verbose_name='Электронная почта')),
                ('idTeacher', models.CharField(max_length=4000, verbose_name='id учителя')),
                ('number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('pole1', models.TextField(default='0', verbose_name='Поле1')),
                ('pole2', models.TextField(default='0', verbose_name='Поле2')),
                ('pole3', models.TextField(default='0', verbose_name='Поле3')),
                ('pole4', models.TextField(default='0', verbose_name='Поле4')),
                ('pole5', models.TextField(default='0', verbose_name='Поле5')),
            ],
        ),
    ]