from flask import Flask, render_template, request, redirect, url_for, flash

from thermos import app, db
from forms import BookmarkForm
from models import Bookmark, User


# Fake login
def logged_user():
    return User.query.filter_by(username='alex').first()


@app.route('/')
@app.route('/index')
def index():
    # app.logger.debug(app.config)  # @TODO print in debug mode
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=logged_user(), url=url, description=description)
        db.session.add(bm) # TODO the object has been aleady added through manage.initdb
        db.session.commit()
        flash('Stored bookmark "{}"'.format(url))
        app.logger.debug('strored url: ' + url) # @TODO print in debug mode
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500