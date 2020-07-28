# Generated by Django 3.0.6 on 2020-07-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20200728_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fy2020_2021',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.AddField(
            model_name='staff',
            name='Code',
            field=models.AutoField(default='default', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='First_Name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Last_Name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
