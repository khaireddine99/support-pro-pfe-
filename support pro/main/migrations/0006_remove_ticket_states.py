# Generated by Django 4.1.5 on 2023-04-06 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ticket_states'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='states',
        ),
    ]
