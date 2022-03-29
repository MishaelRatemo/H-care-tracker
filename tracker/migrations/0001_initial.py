# Generated by Django 4.0.3 on 2022-03-29 13:49

import cloudinary.models
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
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=200)),
                ('dispatch', models.PositiveIntegerField(default=0)),
                ('contact', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price_bought', models.FloatField(default=0)),
                ('reimbursement', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ManyToManyField(related_name='Items', to='tracker.item')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='storages',
            field=models.ManyToManyField(related_name='Storage', to='tracker.store'),
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('donor_name', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='tracker.donor')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.store')),
            ],
        ),
        migrations.AddField(
            model_name='donor',
            name='hospital_name',
            field=models.ManyToManyField(to='tracker.hospital'),
        ),
        migrations.AddField(
            model_name='donor',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.item'),
        ),
    ]
