# Generated by Django 3.1.7 on 2021-03-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0003_auto_20210310_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='ak_mailer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]