# Generated by Django 4.1.4 on 2022-12-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getstarted', '0002_rename_wl_tictac_indexes0f0_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tictac',
            old_name='Indexes0f0',
            new_name='IndexO',
        ),
        migrations.RenameField(
            model_name='tictac',
            old_name='Indexes0fX',
            new_name='IndexX',
        ),
    ]