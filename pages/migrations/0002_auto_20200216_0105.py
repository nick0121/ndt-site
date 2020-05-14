# Generated by Django 2.2.8 on 2020-02-16 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('towers', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='bimini',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='towers.BiminiOrder'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Orders'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Products'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='tower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='towers.TowerOrder'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Customers'),
        ),
        migrations.AddField(
            model_name='address',
            name='dealer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Dealers'),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetails',
            unique_together={('order', 'product')},
        ),
    ]
