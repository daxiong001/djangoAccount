# Generated by Django 4.0.6 on 2022-07-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanage', '0002_alter_account_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=32, verbose_name='用户名')),
                ('passWord', models.CharField(max_length=64, verbose_name='密码')),
            ],
            options={
                'db_table': 'admin',
            },
        ),
    ]