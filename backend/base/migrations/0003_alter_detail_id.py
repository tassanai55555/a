# Generated by Django 4.2.5 on 2023-09-14 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_detail_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.user', unique=True),
        ),
    ]
