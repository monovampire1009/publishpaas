# Generated by Django 4.0.5 on 2022-06-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='d_key',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='e_key',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='n_key',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
