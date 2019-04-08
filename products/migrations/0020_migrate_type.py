from django.db import migrations


def forwards_type(apps, schema_editor):
    """Assert all uuids are unique."""
    product_class = apps.get_model('products', 'Product')
    category_class = apps.get_model('products', 'Category')
    db_alias = schema_editor.connection.alias
    try:
        oil_standard = category_class.objects.using(db_alias).get(name='OIL_STANDARD')
        gas_standard = category_class.objects.using(db_alias).get(name='GAS_STANDARD')
        oil_condensing = category_class.objects.using(db_alias).get(name='OIL_CONDENSING')
        gas_condensing = category_class.objects.using(db_alias).get(name='GAS_CONDENSING')
    except category_class.DoesNotExist:
        return
    for product in product_class.objects.using(db_alias).all():
        if product.type == 'calorificvalue' and product.style == 'oil':
            product.category = oil_standard
        if product.type == 'calorificvalue' and product.style == 'gas':
            product.category = gas_standard
        if product.type == 'condensing' and product.style == 'oil':
            product.category = oil_condensing
        if product.type == 'condensing' and product.style == 'gas':
            product.category = gas_condensing
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20190403_1209'),
    ]

    operations = [
        migrations.RunPython(forwards_type,
                             migrations.RunPython.noop),
    ]
