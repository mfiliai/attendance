# Generated by Django 3.0.6 on 2020-07-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Code', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Position', models.CharField(max_length=200, null=True)),
                ('Band', models.CharField(max_length=20, null=True)),
                ('Date_Created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
