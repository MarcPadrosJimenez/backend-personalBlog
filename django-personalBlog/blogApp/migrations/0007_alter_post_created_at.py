# Generated by Django 5.1.4 on 2025-01-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
