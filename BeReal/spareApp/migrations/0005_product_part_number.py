# Generated by Django 4.2.4 on 2023-08-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareApp', '0004_rename_branch_name_sale_branch_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='part_number',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]