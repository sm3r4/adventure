# Generated by Django 4.2.5 on 2023-09-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advapp', '0012_rename_reg_age_advreg_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='adv_img',
            field=models.URLField(),
        ),
    ]
