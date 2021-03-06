# Generated by Django 3.1.7 on 2022-06-09 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRequest',
            fields=[
                ('pr_no', models.AutoField(primary_key=True, serialize=False)),
                ('pr_status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Withdrawn', 'Withdrawn')], max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('alternative_phone', models.CharField(max_length=11)),
                ('website', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRequestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('item_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='procureoffice.product')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=100)),
                ('delivery_date', models.DateField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='procureoffice.product')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('purchase_order_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date_issued', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='procureoffice.supplier')),
            ],
        ),
    ]
