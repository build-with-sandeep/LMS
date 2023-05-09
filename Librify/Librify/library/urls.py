from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, LibrarianViewSet , BookViewSet , signup

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'librarians', LibrarianViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('signup/', signup, name='signup'),
]
