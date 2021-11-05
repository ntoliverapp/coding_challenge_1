# Generated by Django 3.1.7 on 2021-03-10 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0001_template_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmailEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('preview_text', models.CharField(max_length=255)),
                ('from_line', models.CharField(max_length=255)),
                ('reply_to', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('approved', models.BooleanField()),
                ('tags', models.ManyToManyField(related_name='email_editions', to='templates_app.Tag')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='templates_app.template')),
            ],
        ),
    ]