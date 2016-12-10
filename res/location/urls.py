from django.conf.urls import url
from location import views

urlpatterns = [
	url(r'^country/get/all/$',views.country_list,name='all_country'),
	url(r'^country/get/(?P<pk>[0-9]+)$',views.country_list_with_pk,name='single_country'),
	# url(r'^country/get/all/$',views.CountryListView.as_view(),name='all_country'),
	# url(r'^country/get/(?P<pk>[0-9]+)$',views.CountryListView.as_view(),name='single_country'),
	url(r'^state/get/all/$',views.state_list,name='all_state'),
	url(r'^state/get/(?P<pk>[0-9]+)$',views.state_list_with_pk,name='single_state'),
	url(r'^city/get/all/$',views.city_list,name='all_city'),
	url(r'^city/get/(?P<pk>[0-9]+)$',views.city_list_with_pk,name='single_city'),
]