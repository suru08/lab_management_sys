# Generated by Django 3.2.13 on 2022-07-02 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_student_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admin_id',
        ),
    ]