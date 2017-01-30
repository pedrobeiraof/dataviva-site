from flask import g
from dataviva.apps.embed.views import get_graphs_title
from test_base import BaseTestCase


class GraphsTitlesTests(BaseTestCase):

    def setUp(self):
        g.locale = 'pt'

    def test_titles_graphs_not_is_null(self):
        assert len(get_graphs_title()) > 0;

    def test_titles_graphs_is_a_string(self):
        assert type(get_graphs_title()) == str;
