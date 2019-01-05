# Generated by Django 2.1.2 on 2019-01-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181229_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, default=None, max_length=12, null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='آدرس'),
        ),
    ]
