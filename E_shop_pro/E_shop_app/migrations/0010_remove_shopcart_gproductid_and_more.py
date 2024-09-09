# Generated by Django 4.0 on 2022-06-30 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop_app', '0009_shopcheckout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='Gproductid',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='Lproductid',
        ),
        migrations.CreateModel(
            name='shopCartL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('Lproductid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='E_shop_app.lpro_db')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='E_shop_app.userreg')),
            ],
        ),
        migrations.CreateModel(
            name='shopCartG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('Gproductid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='E_shop_app.product')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='E_shop_app.userreg')),
            ],
        ),
    ]
