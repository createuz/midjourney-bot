# Generated by Django 4.1.4 on 2023-01-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(blank=True, default='Nomalum', max_length=40, null=True, verbose_name='Username'),
        ),
    ]
