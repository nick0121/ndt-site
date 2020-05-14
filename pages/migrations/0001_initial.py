# Generated by Django 2.2.8 on 2020-02-16 06:05

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=20)),
                ('zipCode', models.CharField(max_length=20, verbose_name='Zip/Postal Code')),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('secondary_phone', phone_field.models.PhoneField(blank=True, help_text='Secondary phone number', max_length=31)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('review', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dealer_of', models.CharField(choices=[('none', 'select a manufacturer'), ('mastercraft', 'Mastercraft'), ('moomba', 'Moomba'), ('stingray', 'Stingray'), ('cobalt', 'Cobalt'), ('bryant', 'Bryant'), ('four winns', 'Four Winns'), ('sea doo', 'Sea Doo'), ('malibu', 'Malibu'), ('bayliner', 'Bayliner'), ('starcraft', 'Startcraft'), ('centurion', 'Centurion'), ('tige', 'Tige'), ('nautique', 'Nautique'), ('yamaha', 'Yamaha'), ('supra', 'Supra'), ('ndt', 'NDT'), ('not_listed', 'Not Listed')], max_length=100, verbose_name='Manufacturer')),
                ('contactName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('has_ordered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Dealers',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'OrderDetails',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateOrdered', models.DateTimeField()),
                ('comments', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Customers')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('tower', 'Tower'), ('bimini', 'Bimini'), ('gear', 'Gear'), ('board_rack', 'Board Racks'), ('accessory', 'Accessory')], default='accessory', max_length=50, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
                ('length', models.PositiveSmallIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
                ('sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrdered', models.DateTimeField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comments', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Orders')),
            ],
            options={
                'verbose_name': 'Shipping',
            },
        ),
    ]
