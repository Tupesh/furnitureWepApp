# Generated by Django 4.2.1 on 2023-06-05 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_alter_chaukos_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chaukos',
            name='grade',
        ),
    ]
