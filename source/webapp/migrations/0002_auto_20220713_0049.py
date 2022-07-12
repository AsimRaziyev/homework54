# Generated by Django 3.2.13 on 2022-07-12 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.statuses', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.types', verbose_name='Тип'),
        ),
    ]
