from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Invite, PlaceShips, Shoot, NotifyShotResult, GameOver

urlpatterns = [
    # invite
    url(r'^invite$', Invite.as_view()),
    # place ships
    url(r'^place-ships$', PlaceShips.as_view()),
    # shoot
    url(r'^shoot$', Shoot.as_view()),
    # get shoot result
    url(r'^notify$', NotifyShotResult.as_view()),
    # game over
    url(r'^game-over$', GameOver.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)