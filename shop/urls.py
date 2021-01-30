from django.urls import path
from.import views

urlpatterns = [  path("",views.index,name="ShopHome"),
                 path("about/",views.about,name="About us"),
                 path("contact/",views.contact,name="contact us"),
                 path("tracker/",views.tracker,name="tracker"),
                 path("search/",views.search,name="search"),
                 path("productview/",views.productView,name="productview"),
                 path("checkout/",views.checkout,name="checkout"),

] 