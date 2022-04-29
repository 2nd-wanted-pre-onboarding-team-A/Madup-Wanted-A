# Generated by Django 3.2.6 on 2022-04-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20220428_2203'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='result_data_set',
            index=models.Index(fields=['advertiser', 'date'], name='ads_result__adverti_8fb98d_idx'),
        ),
        migrations.AddIndex(
            model_name='result_data_set',
            index=models.Index(fields=['media'], name='ads_result__media_e39b19_idx'),
        ),
    ]