# Generated by Django 2.1.2 on 2018-12-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emm', '0004_emailregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailemm',
            name='email_register',
            field=models.ManyToManyField(blank=True, null=True, related_name='emailEmm_email_register', to='emm.EmailRegister', verbose_name='انتخاب ایمیل از لیست خبرنامه'),
        ),
    ]
