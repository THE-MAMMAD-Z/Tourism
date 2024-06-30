# Generated by Django 5.0.6 on 2024-06-30 18:50

import django.db.models.deletion
import location_field.models.plain
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=250)),
                ('email', models.EmailField(default='default@gmail.com', max_length=254)),
                ('message', models.TextField(default='default message for models')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=250)),
                ('email', models.EmailField(default='default@gmail.com', max_length=254)),
                ('message', models.TextField(default='default message for models')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('subject', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('rate', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='places/')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('location_type', models.CharField(choices=[('Rs', 'Restaurant'), ('Pr', 'Park'), ('Zo', 'Zoo'), ('Mu', 'Museum'), ('Am', 'Amusement Park'), ('Ma', 'Mall'), ('Tw', 'Tower'), ('Hi', 'Historical'), ('Ot', 'Other')], max_length=3)),
            ],
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.CheckConstraint(check=models.Q(('rate__lte', 5)), name='rate_lte_5'),
        ),
        migrations.AddField(
            model_name='comment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.place'),
        ),
    ]
