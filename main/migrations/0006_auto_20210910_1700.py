# Generated by Django 3.2.6 on 2021-09-10 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_creditentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondpage',
            name='transDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='accountBottom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='network1',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='pstKey',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='purchasingDoc1',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='quantity1',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='taxCode',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='creditentry',
            name='taxJur',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='debitentry',
            name='bLineDate',
            field=models.DateField(default='10/09/2021'),
        ),
        migrations.AlterField(
            model_name='secondpage',
            name='postDate',
            field=models.DateField(default='10/09/2021'),
        ),
    ]