# Generated by Django 5.0 on 2023-12-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pod', '0002_pod_member_podid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pod_transaction',
            name='podid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pod_transaction',
            name='podmemberName',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
