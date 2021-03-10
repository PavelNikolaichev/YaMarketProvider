from django.urls import path
from main.views import OfferDetails, OfferEdit, OfferList

urlpatterns = [
    path('', OfferList.as_view(), name='catalogue_list'),
    path('<shopSku>/', OfferDetails.as_view(), name='offer_by_sku'),
    path('<shopSku>/edit/', OfferEdit.as_view(), name='offer_by_sku_edit')
]