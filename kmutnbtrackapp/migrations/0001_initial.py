# Generated by Django 3.0.6 on 2020-05-29 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.TextField(blank=True)),
                ('time', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmutnbtrackapp.User')),
            ],
        ),
    ]