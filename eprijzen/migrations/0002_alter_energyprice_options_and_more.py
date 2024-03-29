# Generated by Django 4.2.9 on 2024-01-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eprijzen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='energyprice',
            options={'ordering': ['country_id', '-date', '-time'], 'verbose_name': 'Energyprice', 'verbose_name_plural': 'Energy prices'},
        ),
        migrations.AlterIndexTogether(
            name='energyprice',
            index_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='gasprice',
            index_together=set(),
        ),
        migrations.AlterField(
            model_name='energyprice',
            name='all_in_price',
            field=models.FloatField(blank=True, default=None, help_text='Inkoopprijs + inkoopvergoeding + ODE + energiebelasting + BTW', null=True, verbose_name='All-in Price'),
        ),
        migrations.AlterField(
            model_name='energyprice',
            name='extra_fee_price',
            field=models.FloatField(blank=True, default=None, help_text='Inkoopprijs + inkoopvergoeding + BTW', null=True, verbose_name='Extra Fee Price'),
        ),
        migrations.AlterField(
            model_name='energyprice',
            name='purchase_price',
            field=models.FloatField(default=None, help_text='Inkoopprijs', null=True, verbose_name='Purchase Price'),
        ),
        migrations.AlterField(
            model_name='gasprice',
            name='all_in_price',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='All-in Price'),
        ),
        migrations.AlterField(
            model_name='gasprice',
            name='extra_fee_price',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Extra Fee Price'),
        ),
        migrations.AlterField(
            model_name='gasprice',
            name='purchase_price',
            field=models.FloatField(default=None, null=True, verbose_name='Purchase Price'),
        ),
        migrations.AlterUniqueTogether(
            name='energyprice',
            unique_together={('country_id', 'date', 'time')},
        ),
        migrations.AlterUniqueTogether(
            name='gasprice',
            unique_together={('country_id', 'date', 'time')},
        ),
        migrations.AddIndex(
            model_name='energyprice',
            index=models.Index(fields=['country_id'], name='eprijzen_en_country_b2fed6_idx'),
        ),
        migrations.AddIndex(
            model_name='energyprice',
            index=models.Index(fields=['date'], name='eprijzen_en_date_831490_idx'),
        ),
        migrations.AddIndex(
            model_name='energyprice',
            index=models.Index(fields=['time'], name='eprijzen_en_time_53a97f_idx'),
        ),
        migrations.AddIndex(
            model_name='energyprice',
            index=models.Index(fields=['country_id', 'date', 'time'], name='eprijzen_en_country_afe14b_idx'),
        ),
        migrations.AddIndex(
            model_name='gasprice',
            index=models.Index(fields=['country_id'], name='eprijzen_ga_country_798de0_idx'),
        ),
        migrations.AddIndex(
            model_name='gasprice',
            index=models.Index(fields=['date'], name='eprijzen_ga_date_fb5c34_idx'),
        ),
        migrations.AddIndex(
            model_name='gasprice',
            index=models.Index(fields=['time'], name='eprijzen_ga_time_66c3ef_idx'),
        ),
        migrations.AddIndex(
            model_name='gasprice',
            index=models.Index(fields=['country_id', 'date', 'time'], name='eprijzen_ga_country_583d01_idx'),
        ),
    ]
