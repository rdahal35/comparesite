# Generated by Django 2.0.3 on 2018-03-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_auto_20180327_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='mobile_extraFeature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.extraFeatures'),
        ),
    ]
