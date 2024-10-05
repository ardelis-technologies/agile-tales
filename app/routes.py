from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    # Mock data for products
    products = [
        {'id': 1, 'name': 'Product A'},
        {'id': 2, 'name': 'Product B'},
        {'id': 3, 'name': 'Product C'},
    ]
    return render_template('dashboard.html', products=products)

@main.route('/product/<int:product_id>')
def story_map(product_id):
    # Mock data for story map
    story_map = {
        'name': f'Product {product_id} Story Map',
        'stories': [
            {'id': 1, 'title': 'User Story 1'},
            {'id': 2, 'title': 'User Story 2'},
            {'id': 3, 'title': 'User Story 3'},
        ]
    }
    return render_template('story_map.html', story_map=story_map)
