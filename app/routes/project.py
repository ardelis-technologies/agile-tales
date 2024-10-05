from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
# Import your Project model here once it's created
# from app.models import Project

bp = Blueprint('project', __name__)

@bp.route('/projects')
@login_required
def index():
    # Fetch projects here once you have the model set up
    # projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template('project/index.html', projects=[])  # Pass empty list for now

@bp.route('/projects/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Create project logic here
        flash('Project created successfully!', 'success')
        return redirect(url_for('project.index'))
    return render_template('project/create.html')

# Add more routes for viewing, editing, and deleting projects
