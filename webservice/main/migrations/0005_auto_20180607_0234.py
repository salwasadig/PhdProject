# Generated by Django 2.0.5 on 2018-06-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180607_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectfeature',
            old_name='predected',
            new_name='DT_predected',
        ),
        migrations.AddField(
            model_name='projectfeature',
            name='RF_predected',
            field=models.IntegerField(null=True),
        ),
    ]