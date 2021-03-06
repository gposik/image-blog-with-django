# Generated by Django 3.1.3 on 2021-01-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210118_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background_color',
            field=models.CharField(choices=[('Verde bosque', '#00A056'), ('Rosa', '#FFA1A1'), ('Verde manzana', '#9CD484'), ('Amarillo', '#FDAE00'), ('Musgo', '#68735D')], default='Verde bosque', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
