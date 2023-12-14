# Generated by Django 5.0 on 2023-12-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptionChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OI_calls', models.IntegerField()),
                ('CHNG_IN_OI_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VOLUME_calls', models.IntegerField()),
                ('IV_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('LTP_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CHNG_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BID_QTY_calls', models.IntegerField()),
                ('BID_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ASK_calls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ASK_QTY_calls', models.IntegerField()),
                ('STRIKE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BID_QTY_puts', models.IntegerField()),
                ('BID_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ASK_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ASK_QTY_puts', models.IntegerField()),
                ('CHNG_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('LTP_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IV_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VOLUME_puts', models.IntegerField()),
                ('CHNG_IN_OI_puts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OI_puts', models.IntegerField()),
            ],
        ),
    ]
