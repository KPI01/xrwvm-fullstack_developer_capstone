# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='register', view=views.registration, name='register'),

    path(route='get_cars', view=views.get_cars, name ='get_cars'),

    # path for dealer reviews view
    path(route="get_dealer", view=views.get_dealerships, name="get_dealerships"),
    path(route="get_dealer/<str:state>", view=views.get_dealerships, name="get_dealers_by_state"),
    path(route="dealer/<str:dealer_id>", view=views.get_dealer_details, name="dealer_details"),
    path("dealers/", TemplateView.as_view(template_name="index.html")),

    # path for add a review view
    path(route="reviews/dealer/<int:dealer_id>", view=views.get_dealer_reviews, name="dealer_details"),
    path(route="add_review", view=views.add_review, name="add_review"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
