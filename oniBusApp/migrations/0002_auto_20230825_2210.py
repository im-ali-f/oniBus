# Generated by Django 3.2.20 on 2023-08-25 18:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oniBusApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boughttickets',
            name='ownerUser',
            field=models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.SET_NULL, to='oniBusApp.users'),
        ),
        migrations.AddField(
            model_name='boughttickets',
            name='ticket',
            field=models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.SET_NULL, to='oniBusApp.ticket'),
        ),
        migrations.AddField(
            model_name='buss',
            name='VIP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buss',
            name='busType',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='buss',
            name='ownerCompanyorPersonName',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='buss',
            name='seatsNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='destinations',
            name='destName',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='ticket',
            name='bus',
            field=models.ForeignKey(default='0', null=True, on_delete=django.db.models.deletion.SET_NULL, to='oniBusApp.buss'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='departureDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='departureTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='finalDestination',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='ticket',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='origin',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ownerCompany',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='oniBusApp.users'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default='0', max_length=254),
        ),
        migrations.AddField(
            model_name='users',
            name='firstname',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='isCompanyAdmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buss',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='ticket',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='oniBusApp.ticket'),
        ),
    ]
