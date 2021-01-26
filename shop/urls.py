from django.urls import path
from.import views

urlpatterns = [  path("",views.index,name="ShopHome"),
                 path("about/",views.index,name="About us"),
                 path("contact/",views.index,name="contact us"),
                 path("tracker/",views.index,name="tracker"),
                 path("search/",views.index,name="search"),
                 path("productview/",views.index,name="productview"),
                 path("checkout/",views.index,name="checkout"),

] 