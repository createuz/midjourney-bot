# Generated by Django 4.1.4 on 2023-03-26 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0002_alter_telegramuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(choices=[('midjourney', 'Midjourney'), ('googletrans', 'Googletrans')], max_length=100, verbose_name='API nomi'),
        ),
    ]
