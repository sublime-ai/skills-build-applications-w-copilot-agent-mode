from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, distance=1.5)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
    def test_activity_str(self):
        self.assertIn('Test User', str(self.activity))
    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))
