from django.urls import include,path

from rest_framework import routers
from company.views import CompanyViewset,EmployeeViewset

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewset)
router.register(r'employee',EmployeeViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls))
    
]
