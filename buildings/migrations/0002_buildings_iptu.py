# Generated by Django 4.1.2 on 2022-10-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildings',
            name='iptu',
            field=models.FloatField(default=1.11),
            preserve_default=False,
        ),
    ]