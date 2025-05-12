from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemSerializer
    # cache list (GET api/items/) for 60s
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
