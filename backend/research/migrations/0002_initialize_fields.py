from django.db import migrations, transaction


class Migration(migrations.Migration):
    dependencies = [
        ('research', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from research.models import ResearchField
        test_data = ['Brain',
                     'Arm']

        with transaction.atomic():
            for name in test_data:
                field = ResearchField(name=name)
                field.save()

    operations = [
        migrations.RunPython(generate_data),
    ]
