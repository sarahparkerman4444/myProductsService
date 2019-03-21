from rest_framework import routers

from products import views


router = routers.SimpleRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'property', views.PropertyViewSet)

urlpatterns = router.urls
