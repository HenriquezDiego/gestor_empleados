from django.core.management import call_command
from django.db import migrations

AREAS = [
    {
        'nombre': 'Desarrollo de Software',
        'subareas': ['Frontend', 'Backend', 'Full Stack']
    },
    {
        'nombre': 'Diseño de Interfaz',
        'subareas': ['UI Design', 'UX Design']
    },
    {
        'nombre': 'QA y Pruebas',
        'subareas': ['Pruebas Funcionales', 'Pruebas de Rendimiento']
    },
    # Agrega más áreas y subáreas según sea necesario
]

def seed_data(apps, schema_editor):
    Area = apps.get_model('empleados_api', 'Area')
    SubArea = apps.get_model('empleados_api', 'SubArea')
    for area_data in AREAS:
        area = Area.objects.create(nombre=area_data['nombre'])
        for subarea_name in area_data['subareas']:
            SubArea.objects.create(nombre=subarea_name, area=area)

class Migration(migrations.Migration):

    dependencies = [
        ('empleados_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]