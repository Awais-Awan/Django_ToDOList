from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,logout_view,RegisterPage

urlpatterns = [
    path("login/", CustomLoginView.as_view() ,name="login" ),
    path("logout/", logout_view,name="logout" ),
    path("register/", RegisterPage.as_view(),name="register" ),



    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("taskcreate/", TaskCreate.as_view(), name="taskcreate"),
    path("taskupdate/<int:pk>", TaskUpdate.as_view(), name="taskupdate"),
    path("taskdelete/<int:pk>", TaskDelete.as_view(), name="taskdelete"),
]
