# Generated by Django 4.1 on 2022-08-13 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phoneCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shipping_type', models.CharField(max_length=100)),
                ('container_no', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('heig', models.IntegerField()),
                ('weig', models.IntegerField()),
                ('goodsType', models.CharField(blank=True, max_length=100)),
                ('additional_info', models.CharField(blank=True, max_length=100)),
                ('pickup_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('arrival_timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_doc_id', models.IntegerField()),
                ('reference_no', models.IntegerField()),
                ('doc_url', models.CharField(max_length=100)),
                ('document_name', models.CharField(max_length=100)),
                ('shipment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingFrom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_company', models.CharField(max_length=100)),
                ('sender_country', models.CharField(max_length=100)),
                ('sender_address', models.CharField(max_length=100)),
                ('sender_address_2', models.CharField(max_length=100)),
                ('sender_address_3', models.CharField(max_length=100)),
                ('postal_code', models.BigIntegerField(null=True)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField(null=True)),
                ('country_code', models.BigIntegerField(null=True)),
                ('taxt_no', models.BigIntegerField(null=True)),
                ('vat_no', models.IntegerField(null=True)),
                ('shipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_app.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_name', models.CharField(max_length=100)),
                ('receiver_company', models.CharField(max_length=100)),
                ('receiver_country', models.CharField(max_length=100)),
                ('receiver_address', models.CharField(max_length=100)),
                ('receiver_address_2', models.CharField(max_length=100)),
                ('receiver_address_3', models.CharField(max_length=100)),
                ('postal_code', models.BigIntegerField(null=True)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField(null=True)),
                ('country_code', models.BigIntegerField(null=True)),
                ('taxt_no', models.IntegerField(null=True)),
                ('shipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery_app.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_no', models.CharField(default='564277855801', max_length=12, unique=True)),
                ('tracking_description', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('quantity', models.CharField(max_length=100)),
                ('delivered', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100, null=True)),
                ('estdeliveryDate', models.CharField(max_length=100, null=True)),
                ('shipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipment_key', to='delivery_app.shipment')),
                ('shipping_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shippingfrom_key', to='delivery_app.shippingfrom')),
                ('shipping_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shippingto_key', to='delivery_app.shippingto')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_app.state')),
            ],
        ),
    ]
