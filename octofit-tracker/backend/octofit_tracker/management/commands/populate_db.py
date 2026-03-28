from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Run', duration=30, distance=5),
            Activity(user=users[1], type='Swim', duration=45, distance=2),
            Activity(user=users[2], type='Bike', duration=60, distance=20),
            Activity(user=users[3], type='Run', duration=25, distance=4),
            Activity(user=users[4], type='Swim', duration=50, distance=2.5),
            Activity(user=users[5], type='Bike', duration=70, distance=25),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            Workout(name='Morning Cardio', description='Cardio for all heroes'),
            Workout(name='Strength Training', description='Strength for all heroes'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=140)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
