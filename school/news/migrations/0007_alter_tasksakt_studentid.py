# Generated by Django 3.2.16 on 2023-09-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20230816_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksakt',
            name='studentId',
            field=models.CharField(max_length=100, verbose_name='Логин ученика'),
        ),
    ]