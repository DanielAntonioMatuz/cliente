# Generated by Django 2.2.1 on 2020-02-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='estadoCivil',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
