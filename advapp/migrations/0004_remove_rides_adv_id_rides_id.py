# Generated by Django 4.2.5 on 2023-09-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advapp', '0003_remove_rides_id_rides_adv_desc_rides_adv_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rides',
            name='adv_id',
        ),
        migrations.AddField(
            model_name='rides',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
