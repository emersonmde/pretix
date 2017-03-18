# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 17:48
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0051_auto_20170206_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_count', models.PositiveIntegerField(default=0, verbose_name='Minimum number')),
                ('max_count', models.PositiveIntegerField(default=1, verbose_name='Maximum number')),
            ],
        ),
        migrations.AddField(
            model_name='cartposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.CartPosition'),
        ),
        migrations.AddField(
            model_name='itemcategory',
            name='is_addon',
            field=models.BooleanField(default=False, help_text='If selected, the products belonging to this category are not for sale on their own. They can only be bought in combination with a product that has this category configured as a possible source for add-ons.', verbose_name='Products in this category are add-on products'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.OrderPosition'),
        ),
        migrations.AlterField(
            model_name='item',
            name='allow_cancel',
            field=models.BooleanField(default=True, help_text='If this is active and the general event settings allo wit, orders containing this product can be canceled by the user until the order is paid for. Users cannot cancel paid orders on their own and you can cancel orders at all times, regardless of this setting', verbose_name='Allow product to be canceled'),
        ),
        migrations.AlterField(
            model_name='item',
            name='default_price',
            field=models.DecimalField(decimal_places=2, help_text='If this product has multiple variations, you can set different prices for each of the variations. If a variation does not have a special price or if you do not have variations, this price will be used.', max_digits=7, null=True, verbose_name='Default price'),
        ),
        migrations.AddField(
            model_name='itemaddon',
            name='addon_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addon_to', to='pretixbase.ItemCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='itemaddon',
            name='base_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addons', to='pretixbase.Item'),
        ),
    ]