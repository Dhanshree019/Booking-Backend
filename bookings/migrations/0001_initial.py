# Generated by Django 5.1.7 on 2025-03-20 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('contact_number', models.CharField(blank=True, max_length=16, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bus_operator',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(help_text='Duration of the trip in HH:MM:SS format')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'route',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'stop',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('bus_type', models.CharField(choices=[('sleeper', 'Sleeper'), ('sitting', 'Sitting'), ('both', 'Both')], max_length=10)),
                ('sitting_seats', models.PositiveIntegerField()),
                ('sleeper_seats', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buses', to='bookings.busoperator')),
            ],
            options={
                'db_table': 'bus',
            },
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bookings.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bookings.route')),
            ],
            options={
                'db_table': 'bus_schedule',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('seat_type', models.CharField(choices=[('sleeper', 'Sleeper'), ('sitting', 'Sitting')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='bookings.bus')),
            ],
            options={
                'db_table': 'seat',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=16, unique=True)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bookings.busschedule')),
                ('seats', models.ManyToManyField(related_name='bookings', to='bookings.seat')),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_destination', to='bookings.stop'),
        ),
        migrations.AddField(
            model_name='route',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_source', to='bookings.stop'),
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(help_text='All stops including source & destination', related_name='routes', to='bookings.stop'),
        ),
    ]
