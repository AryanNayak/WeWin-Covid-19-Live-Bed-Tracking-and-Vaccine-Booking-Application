from django.urls import path, include   
from . import views













urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    # path('subject-detail/user_id=<str:user>/subject_id=<int:id>',
    #      views.subjectDetail, name="subject-detail"),
    path('hospital-list/state=<str:state>/',
         views.hospitalList, name="hospital-list"),
  path('hospital-detail/hospitalID=<str:hospitalID>/',
         views.hospitalDetail, name="hospital-detail"),
path('hospital-update/hospitalID=<str:hospitalID>/added=<str:added>/',
         views.hospitalUpdate, name="hospital-update"),
path('patient-update/',
         views.patientHealthUpdate, name="patient-update"),

    # path('user-recommend/user name=<str:username>/', views.recommendUsers, name="recommendUsers"),
    path('hospital-login/username=<str:hospitalID>/password=<str:password>/'     # >/password=<str:password>'
         ,views.hospitalLogin, name="hospital-login"),

    # # # path('subject-detail/<str:pk>/', views.subjectDetail, name="subject-detail"),
    # path('post-insert/',
    #      views.postInsert, name="post-insert"),
    path('hospital-register/', views.hospitalRegistration, name="hospital-registration"),
    # path('user-follow/', views.userFollow, name="user-follow"),
    path('hospital-updateBeds/hospitalID=<int:hospitalID>/incr=<int:incr>/', views.updateBeds, name="hospital-updateBeds"),

    path('patientHealthUpdate/',
         views.patientHealthUpdate, name="patientHealthUpdate"),
    # # path('subject-delete/subjectId=<str:subjectId>/',
    # #      views.subjectDelete, name="subject-delete"),
]
