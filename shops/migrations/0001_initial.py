# Generated by Django 2.2.9 on 2020-08-06 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=140)),
                ('description', models.TextField(blank=True)),
                ('region', models.CharField(blank=True, max_length=80)),
                ('city', models.CharField(blank=True, max_length=80)),
                ('address', models.CharField(blank=True, max_length=80)),
                ('homepage', models.URLField(blank=True, max_length=250)),
                ('phone_number', models.IntegerField(blank=True)),
                ('average', models.IntegerField(blank=True)),
                ('like_users', models.ManyToManyField(related_name='like_shops', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rating', models.SmallIntegerField(blank=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops_rating', to='shops.Shop')),
                ('user', models.ManyToManyField(related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]