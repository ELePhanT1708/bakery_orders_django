from django.urls import path

from .views import order, add_product

urlpatterns = [
    path('order/', order, name='order'),
    path('product/', add_product, name='product'),
    # path('webinars/', ViewWebinars.as_view(), name='webinars'),
    # path('teachers/', ViewTeachers.as_view(), name='teachers'),
    # path('courses/', ViewCourses.as_view(), name='courses'),
    # path('course/add_course', add_course, name='add_course'),
    # path('teacher/add_teacher', add_teacher, name='add_teacher'),
    # path('webinar/add_webinar', add_webinar, name='add_webinar'),
]