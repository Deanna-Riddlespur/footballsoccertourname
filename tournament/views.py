from rest_framework import viewsets

from .serializers import TournamentSerializer, ParticipantSerializer
from .models import Tournament, Participant


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tournament to be viewed or edited.
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participant to be viewed or edited.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
