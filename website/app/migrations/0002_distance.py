# Generated by Django 3.1.2 on 2020-10-05 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.agent')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.rootstate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
