# Generated by Django 3.1.4 on 2021-05-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0003_auto_20210503_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='specification',
            field=models.TextField(null=True),
        ),
    ]