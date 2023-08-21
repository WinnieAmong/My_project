# Generated by Django 4.2.4 on 2023-08-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareApp', '0003_rename_item_name_product_part_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='branch_name',
            new_name='branch',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]