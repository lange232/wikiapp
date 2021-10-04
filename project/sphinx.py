from flask import Blueprint
from flask_login import login_required

sphinx = Blueprint('sphinx', __name__, static_url_path="/", static_folder='../sphinx/build/html/')


@sphinx.route('/wiki')
@sphinx.route('/wiki/<path:path>')
@login_required
def serve_sphinx_docs(path='index.html'):
    return sphinx.send_static_file(path)

