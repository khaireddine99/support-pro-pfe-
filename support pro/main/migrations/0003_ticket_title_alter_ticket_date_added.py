# Generated by Django 4.1.5 on 2023-03-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_ticket_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='zebi', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
