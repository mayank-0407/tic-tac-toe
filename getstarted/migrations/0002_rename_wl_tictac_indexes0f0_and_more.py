# Generated by Django 4.1.4 on 2022-12-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getstarted', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tictac',
            old_name='wl',
            new_name='Indexes0f0',
        ),
        migrations.RenameField(
            model_name='tictac',
            old_name='board',
            new_name='winningIndex',
        ),
        migrations.AddField(
            model_name='tictac',
            name='Indexes0fX',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tictac',
            name='statuss',
            field=models.CharField(default='loss', max_length=5),
        ),
    ]
