from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import StoryMap, UserStory

bp = Blueprint('story_map', __name__)

@bp.route('/story_maps')
@login_required
def index():
    story_maps = StoryMap.query.filter_by(user_id=current_user.id).all()
    return render_template('story_map/index.html', story_maps=story_maps)

@bp.route('/story_maps/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        story_map = StoryMap(title=title, description=description, user_id=current_user.id)
        db.session.add(story_map)
        db.session.commit()
        flash('Story map created successfully!', 'success')
        return redirect(url_for('story_map.index'))
    return render_template('story_map/create.html')

@bp.route('/story_maps/<int:id>')
@login_required
def view(id):
    story_map = StoryMap.query.get_or_404(id)
    if story_map.user_id != current_user.id:
        flash('You do not have permission to view this story map.', 'error')
        return redirect(url_for('story_map.index'))
    return render_template('story_map/view.html', story_map=story_map)

@bp.route('/story_maps/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    story_map = StoryMap.query.get_or_404(id)
    if story_map.user_id != current_user.id:
        flash('You do not have permission to edit this story map.', 'error')
        return redirect(url_for('story_map.index'))

    if request.method == 'POST':
        story_map.title = request.form['title']
        story_map.description = request.form['description']
        db.session.commit()
        flash('Story map updated successfully!', 'success')
        return redirect(url_for('story_map.view', id=story_map.id))

    return render_template('story_map/edit.html', story_map=story_map)

@bp.route('/story_maps/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    story_map = StoryMap.query.get_or_404(id)
    if story_map.user_id != current_user.id:
        flash('You do not have permission to delete this story map.', 'error')
        return redirect(url_for('story_map.index'))

    db.session.delete(story_map)
    db.session.commit()
    flash('Story map deleted successfully!', 'success')
    return redirect(url_for('story_map.index'))
