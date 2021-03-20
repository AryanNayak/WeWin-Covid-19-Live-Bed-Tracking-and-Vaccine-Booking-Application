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

    # path('user-recommend/user name=<str:username>/', views.recommendUsers, name="recommendUsers"),
    path('hospital-login/username=<str:hospitalID>/password=<str:password>/'     # >/password=<str:password>'
         ,views.hospitalLogin, name="hospital-login"),

    # # # path('subject-detail/<str:pk>/', views.subjectDetail, name="subject-detail"),
    # path('post-insert/',
    #      views.postInsert, name="post-insert"),
    path('hospital-register/', views.hospitalRegistration, name="hospital-registration"),
    # path('user-follow/', views.userFollow, name="user-follow"),

    # # path('subject-update/user=<str:user>/subject_id=<int:id>',
    # #      views.subjectUpdate, name="subject-update"),
    # # path('subject-delete/subjectId=<str:subjectId>/',
    # #      views.subjectDelete, name="subject-delete"),
]
