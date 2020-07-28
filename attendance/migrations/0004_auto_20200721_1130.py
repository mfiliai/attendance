# Generated by Django 3.0.6 on 2020-07-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20200721_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fy2020_2021',
            name='Attendance',
            field=models.CharField(choices=[('On Duty', 'On Duty'), ('Late', 'Late'), ('Casual Leave', 'Casual Leave'), ('Annual Leave', 'Annual Leave'), ('Sick Leave', 'Sick Leave'), ('In Lieu', 'In Lieu'), ('NOP', 'NOP')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fy2020_2021',
            name='Last_Name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
