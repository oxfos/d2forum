# Generated by Django 3.0.3 on 2020-04-02 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200402_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='refpost',
            new_name='ref_post',
        ),
    ]