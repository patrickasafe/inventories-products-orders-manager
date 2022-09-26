# Generated by Django 4.0.6 on 2022-09-26 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('ref', models.CharField(max_length=6, verbose_name='Reference')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('quantity', models.IntegerField(verbose_name='Product quantity at Inventory')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_product', to='inventories.inventory', verbose_name='Inventory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_product', to='products.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='products',
            field=models.ManyToManyField(related_name='inventories', through='inventories.InventoryProduct', to='products.product', verbose_name='Products'),
        ),
    ]
