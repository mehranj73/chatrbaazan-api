# Generated by Django 2.1.2 on 2018-12-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usersendcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربران', 'verbose_name_plural': 'کاربران'***REMOVED***,
        ),
        migrations.AlterModelOptions(
            name='usersendcode',
            options={'verbose_name': 'کدهای ارسال کاربران', 'verbose_name_plural': 'کدهای ارسال کاربران'***REMOVED***,
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]
