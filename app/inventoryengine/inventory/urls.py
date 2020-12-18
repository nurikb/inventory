from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from .views import *

urlpatterns = [
    path('admission/', views.AdmissionListView.as_view()),
    path('admission/<int:pk>', views.AdmissionDetailView.as_view()),
    path('addadmission/', views.AddAdmissionView.as_view()),
    path('equipment/', views.EquipmentWorkerListView.as_view()),
    path('equipment/<int:pk>', views.EquipmentWorkerDetailView.as_view()),
    path('type/', views.TypeEquipmentListView.as_view()),
    path('addequipment/', views.EquipmentWorkerCreateView.as_view()),

    path('', AdmissionView.as_view(), name='admissions_url'),
    path('upload/', UploadView.as_view(), name='upload_url'),
    path('upload/delete/', upload_delete, name='upload_delete_url'),
    path('addWorker/', WorkersCreate.as_view(), name='workers_url'),
    path('relocation/', relocation_list, name='relocation_history_url'),
    path('equipmentsForWorkers/', EquipmentViewDelete.as_view(), name='equipmentsForWorkers_url'),
    path('addAdmissions/', AdmissionCreate.as_view(), name='addAdmissions_url'),
    path('assignToWorker/<str:admission_id>/', AssignToWorker.as_view(), name='assign_to_worker_url'),
    path('assignToWorker/<str:admission_id>/update/', AssignToWorkerUpdate.as_view(), name='update_url'),
    path('assignToWorker/<str:admission_id>/qr/', QrCreate.as_view(), name='qr_url'),
    path('export/xls/', Export_xls.as_view(), name='export_users_xls'),
    path('export_workers_xls/xls/', Export_xls_workers.as_view(), name='export_workers_xls'),
    path('export_history_xls/xls/', Export_xls_history.as_view(), name='export_history_xls'),
]

urlpatterns += staticfiles_urlpatterns()
