from app import create_app, db
from app.models import User, StoryMap, UserStory
from werkzeug.security import generate_password_hash

def seed_data():
    app = create_app()
    with app.app_context():
        # Create users
        users = [
            User(username='john_doe', email='john@example.com', password_hash=generate_password_hash('password123')),
            User(username='jane_smith', email='jane@example.com', password_hash=generate_password_hash('password456'))
        ]
        db.session.add_all(users)
        db.session.commit()

        # Create story maps
        story_maps = [
            StoryMap(title='E-commerce Platform', description='User stories for our new e-commerce platform', user_id=users[0].id),
            StoryMap(title='Mobile App Features', description='Feature mapping for our mobile app', user_id=users[1].id)
        ]
        db.session.add_all(story_maps)
        db.session.commit()

        # Create user stories
        user_stories = [
            UserStory(title='User Registration', description='As a new user, I want to register an account', status='New', order=1, story_map_id=story_maps[0].id),
            UserStory(title='Product Search', description='As a customer, I want to search for products', status='In Progress', order=2, story_map_id=story_maps[0].id),
            UserStory(title='Push Notifications', description='As a user, I want to receive push notifications', status='New', order=1, story_map_id=story_maps[1].id),
            UserStory(title='Offline Mode', description='As a user, I want to use the app offline', status='In Progress', order=2, story_map_id=story_maps[1].id)
        ]
        db.session.add_all(user_stories)
        db.session.commit()

        print("Seed data has been added successfully!")

if __name__ == '__main__':
    seed_data()
