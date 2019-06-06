from bonds.viewsets import BondViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bonds', BondViewSet, base_name = 'bonds')
