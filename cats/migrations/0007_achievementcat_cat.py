# Generated by Django 3.2 on 2022-05-16 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_auto_20220516_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementcat',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cats.cat'),
            preserve_default=False,
        ),
    ]
