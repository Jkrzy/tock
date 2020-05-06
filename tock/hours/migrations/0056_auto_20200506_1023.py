# Generated by Django 2.2.12 on 2020-05-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0055_auto_20200430_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Unit'),
        ),
    ]
