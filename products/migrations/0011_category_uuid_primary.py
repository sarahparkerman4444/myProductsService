from django.db import migrations, models
import django.db.models.deletion

import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productcategory_is_global'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='id',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='products.ProductCategory'),
        ),
    ]
