# Generated by Django 2.1.2 on 2018-11-05 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('caracteristicas', models.TextField()),
                ('fecha_fabricacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_caducidad', models.DateTimeField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
