from django.db import migrations, models
import uuid


def forwards_property_uuid(apps, schema_editor):
    """Assert all uuids are unique."""
    Property = apps.get_model('products', 'Property')
    db_alias = schema_editor.connection.alias
    for property in Property.objects.using(db_alias).all():
        property.uuid = uuid.uuid4()
        property.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_category_uuid_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False),
        ),
        migrations.RunPython(forwards_property_uuid,
                             migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='property',
            name='id',
        ),
        migrations.AlterField(
            model_name='property',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='property',
            name='product',
        ),
        migrations.AddField(
            model_name='property',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
