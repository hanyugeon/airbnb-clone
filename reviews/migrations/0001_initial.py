# Generated by Django 2.2.5 on 2021-05-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('accuracy', models.IntegerField()),
                ('location', models.IntegerField()),
                ('comminication', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
