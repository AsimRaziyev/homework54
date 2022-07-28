# Generated by Django 3.2.13 on 2022-07-28 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20220728_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]