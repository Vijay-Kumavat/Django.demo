from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Kvm3 IceCreams Admin"
admin.site.site_title = "Kvm3 IceCreams Admin Portal"
admin.site.index_title = "Welcome to Kvm3 IceCreams  Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]
