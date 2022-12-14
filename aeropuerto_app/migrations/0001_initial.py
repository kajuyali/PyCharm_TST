# Generated by Django 4.1 on 2022-08-25 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_avion', models.CharField(max_length=20, unique=True)),
                ('tipo_avion', models.CharField(max_length=20)),
                ('ciudad_base', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_piloto', models.CharField(max_length=20, unique=True)),
                ('nombre_piloto', models.CharField(max_length=50)),
                ('horas_vuelo_piloto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tripulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_tripulante', models.CharField(max_length=20, unique=True)),
                ('nombre_tripulante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vuelo', models.CharField(max_length=20, unique=True)),
                ('origen', models.CharField(max_length=20)),
                ('destino', models.CharField(max_length=20)),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aeropuerto_app.avion')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aeropuerto_app.piloto')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_tabla', models.CharField(max_length=20, unique=True)),
                ('tripulacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aeropuerto_app.tripulacion')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aeropuerto_app.vuelo')),
            ],
        ),
    ]
