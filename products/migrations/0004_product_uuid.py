from django.db import migrations, models
import uuid


def forwards_product_uuid(apps, schema_editor):
    """Assert all uuids are unique."""
    Product = apps.get_model('products', 'Product')
    db_alias = schema_editor.connection.alias
    for product in Product.objects.using(db_alias).all():
        product.uuid = uuid.uuid4()
        product.save()


def backwards_product_uuid(apps, schema_editor):
    # nothing to do here
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190114_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(forwards_product_uuid,
                             backwards_product_uuid),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        )
    ]
