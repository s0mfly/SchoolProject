# Generated by Django 3.2.16 on 2022-12-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_polzakt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polzakt',
            options={'ordering': ['id'], 'verbose_name': 'Актив пользователей', 'verbose_name_plural': 'Актив пользователей'},
        ),
        migrations.AddField(
            model_name='polzakt',
            name='pole1',
            field=models.TextField(default='0', verbose_name='Поле1'),
        ),
        migrations.AddField(
            model_name='polzakt',
            name='pole2',
            field=models.TextField(default='0', verbose_name='Поле2'),
        ),
        migrations.AddField(
            model_name='polzakt',
            name='pole3',
            field=models.TextField(default='0', verbose_name='Поле3'),
        ),
        migrations.AddField(
            model_name='polzakt',
            name='pole4',
            field=models.TextField(default='0', verbose_name='Поле4'),
        ),
        migrations.AddField(
            model_name='polzakt',
            name='pole5',
            field=models.TextField(default='0', verbose_name='Поле5'),
        ),
        migrations.AlterField(
            model_name='polzakt',
            name='otshist',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
    ]
