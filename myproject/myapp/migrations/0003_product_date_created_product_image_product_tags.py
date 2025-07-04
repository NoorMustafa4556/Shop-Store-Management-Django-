# Generated by Django 5.2.3 on 2025-06-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_remove_customer_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myapp.tag'),
        ),
    ]
