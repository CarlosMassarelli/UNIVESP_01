from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from concentra.auth import login_required
from concentra.db import get_db
from consultando import concent

bp = Blueprint('naoh', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT r.id, temperatura, densidade, concentracao, created, author_id, username'
        ' FROM resultado r JOIN user u ON r.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('naoh/index.html', posts=posts)


@bp.route('/dados', methods=('GET', 'POST'))
# @login_required
def create():
    if request.method == 'POST':
        temperatura = request.form['temperatura']
        densidade = request.form['densidade']
        error = None

        if not temperatura:
            error = 'Temperatura é necessária.'

        if not temperatura.isnumeric():
            error = 'Temperatura deve ser um número'

        temperatura = int(temperatura)
        densidade = float(densidade)

        concentracao = concent(temperatura, densidade)

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO resultado (temperatura, densidade, concentracao, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (temperatura, densidade, concentracao, g.user['id'])
            )
            db.commit()
            return redirect(url_for('naoh.index'))

    return render_template('naoh/dados.html')

#
# def get_post(id, check_author=True):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()
#
#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")
#
#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
#
#     return post
#
#
# @bp.route('/<int:id>/update', methods=('GET', 'POST'))
# @login_required
# def update(id):
#     post = get_post(id)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
#
#         if not title:
#             error = 'Title is required.'
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'UPDATE post SET title = ?, body = ?'
#                 ' WHERE id = ?',
#                 (title, body, id)
#             )
#             db.commit()
#             return redirect(url_for('consulta.index'))
#
#     return render_template('consulta/update.html', post=post)
#
#
# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     get_post(id)
#     db = get_db()
#     db.execute('DELETE FROM post WHERE id = ?', (id,))
#     db.commit()
#     return redirect(url_for('consulta.index'))
#
