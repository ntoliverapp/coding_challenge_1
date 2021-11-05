# Generated by Django 3.1.7 on 2021-03-18 20:42

from django.db import migrations, models

def to_lower(apps, schema_editor):
    Templates = apps.get_model('templates_app', 'Template')
    for template in Templates.objects.all():
        template.template_type = template.template_type.lower()
        template.name = template.name.lower()
        template.save(update_fields=['template_type','name'])

class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0003_auto_20210310_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.RunPython(to_lower),
    ]