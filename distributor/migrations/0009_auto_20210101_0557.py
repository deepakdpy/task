# Generated by Django 3.1.4 on 2021-01-01 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0004_auto_20210101_0549'),
        ('distributor', '0008_orderbook_orderreader'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderreader',
            name='deliveryaddress',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='nocod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='order/screenshot')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.orderreader')),
            ],
        ),
        migrations.CreateModel(
            name='cod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validcoupon', models.BooleanField(default=False)),
                ('oldbooks', models.BooleanField(default=False)),
                ('express', models.BooleanField(default=False)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.coupon')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.orderreader')),
            ],
        ),
    ]