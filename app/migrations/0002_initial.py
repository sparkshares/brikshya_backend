# Generated by Django 4.2.8 on 2024-01-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treedonationtransaction',
            name='donar_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.donors'),
        ),
    ]