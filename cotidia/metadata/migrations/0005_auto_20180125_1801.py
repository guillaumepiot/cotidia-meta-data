# Generated by Django 2.0.1 on 2018-01-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170903_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membersocial',
            options={'ordering': ('order_id',), 'verbose_name': 'MetaData social network', 'verbose_name_plural': 'MetaData social networks'},
        ),
        migrations.AlterField(
            model_name='member',
            name='order_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
