# Generated by Django 5.0.4 on 2024-04-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='property_type',
            field=models.CharField(choices=[('House', 'House'), ('Apartment Complex', 'Apartment Complex'), ('Apartment Unit', 'Apartment Unit'), ('Condo', 'Condo'), ('Building', 'Building'), ('Land', 'Land'), ('Business', 'Business'), ('Business Suite', 'Business Suite'), ('Shop', 'Shop'), ('Warehouse', 'Warehouse'), ('Storage', 'Storage'), ('Office', 'Office'), ('Other', 'Other')], default='NA', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='square_feet',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='stories',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='street',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='territory',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='zip',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(help_text='Name of the property, street specifically, again.', max_length=100),
        ),
    ]