# Generated by Django 5.0 on 2023-12-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_detail_uniqueuserid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]