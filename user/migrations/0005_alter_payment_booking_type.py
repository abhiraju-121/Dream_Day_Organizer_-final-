# Generated by Django 5.0.4 on 2025-02-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_bookevent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='booking_type',
            field=models.CharField(choices=[('event', 'Event Booking'), ('venue', 'Venue Booking'), ('transport', 'Transport Booking'), ('catering', 'Catering Booking'), ('decoration', 'Decoration Booking'), ('photography', 'Photography Booking'), ('bride_groom', 'Bride_GroomService Booking')], max_length=20),
        ),
    ]
