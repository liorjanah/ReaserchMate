# Generated by Django 4.0.6 on 2022-07-21 20:48

from django.db import migrations, transaction
import random


class Migration(migrations.Migration):
    dependencies = [
        ('participant', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from participant.models import Participant

        with transaction.atomic():
            name_prefix = 'participant'
            for i in range(1, 11):
                name = '{}_{}'.format(name_prefix, i)
                Participant.create(email='{}@gmail.com'.format(name), username=name, password=name,
                                   first_name=name_prefix, last_name=str(i),
                                   phone_number=random.randint(1000000000, 9999999999))

    operations = [
        migrations.RunPython(generate_data),
    ]
