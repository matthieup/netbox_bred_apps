from netbox.api.routers import NetBoxRouter
from . import views

app_name = "netbox_bred_apps"

router = NetBoxRouter()
router.register("bredapplication", views.BredApplicationViewSet)
router.register("bredapplication_detail", views.BredApplicationViewSet)

urlpatterns = router.urls
