# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, request, abort
from dataviva.apps.general.views import get_locale
from dataviva.translations.dictionary import dictionary
import urllib
import json

mod = Blueprint('occugrid', __name__,
                template_folder='templates',
                url_prefix='/<lang_code>/occugrid',
                static_folder='static')


@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.locale = values.pop('lang_code')


@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', get_locale())


@mod.before_request
def before_request():
    g.page_type = mod.name

# cicle is occupation ever, the cnae is change,   
@mod.route('/<industry>')
def index(industry="14126"):
    return render_template('occugrid/index.html',
                           industry=industry,
                           dictionary=json.dumps(dictionary()))
