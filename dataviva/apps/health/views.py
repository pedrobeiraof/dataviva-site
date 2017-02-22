from flask import Blueprint, render_template, g, request, abort
from dataviva.apps.general.views import get_locale

mod = Blueprint('health', __name__,
                template_folder='templates',
                url_prefix='/<lang_code>/health',
                static_folder='static')

@mod.before_request
def before_request():
    g.page_type = 'category'


@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.locale = values.pop('lang_code')


@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', get_locale())

@mod.route('/<id>', defaults={'tab': 'general'})
def index(id, tab):
    total = {
        'beds': 100000,
        'professionals': 100000,
        'equipments': 100000,
        'establishments': 100000,
    }

    return render_template('health/index.html', total=total, tab=tab)

@mod.route('/<id>/graphs/<tab>', methods=['POST'])
def graphs(id, tab):
    return render_template('health/graphs-' + tab + '.html')