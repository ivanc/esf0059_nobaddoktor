from flask import Blueprint
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

public_bp = Blueprint('pages', __name__,
                        template_folder='templates')

@public_bp.route('/pages/', defaults={'page': 'index'})
@public_bp.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)

