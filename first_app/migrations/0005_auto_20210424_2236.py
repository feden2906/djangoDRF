# Generated by Django 3.2 on 2021-04-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210424_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='offices',
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='offices',
            field=models.ManyToManyField(db_column='office_employee', related_name='employee', to='first_app.OfficeModel'),
        ),
    ]
