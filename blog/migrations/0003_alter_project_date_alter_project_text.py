# Generated by Django 4.0.4 on 2022-05-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]
