from django.conf.urls import url
from django.urls import path, include
from tutorials import views
from rest_framework.routers import DefaultRouter
from tutorials.views import TutorialsViewSet


router = DefaultRouter()
router.register(r'tutorials', views.TutorialsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     url(r'^api/tutorials$', views.tutorial_list),
#     url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#     url(r'^api/tutorials/published$', views.tutorial_list_published)
# ]
