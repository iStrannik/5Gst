# Generated by Django 4.0.5 on 2022-07-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField()),
                ('port', models.IntegerField()),
                ('port_iperf', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]