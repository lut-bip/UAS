# Generated by Django 4.2.7 on 2024-01-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutfi', '0003_alter_chatid_options_alter_produk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
