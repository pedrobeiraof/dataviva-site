from flask import Blueprint
from dataviva.apps.embed.models import Build, App


mod = Blueprint('title', __name__,
                template_folder='templates',
                url_prefix='/<lang_code>/title')


def get_graphs_title(type='tree_map', dataset='secex', id_ibge='31', filter1='all', filter2='all', output='bra'):
	title = ''
	bra = id_ibge
	if '_' in id_ibge: # compare
		bra = '<bra>_<bra>'
	elif id_ibge is not 'all':
		bra = '<bra>'

	app = App.query.filter(type==type).first_or_404()
	query = Build.query.filter(Build.app_id==app.id, Build.dataset==dataset, Build.bra==bra, Build.filter1==filter1, Build.filter2==filter2, Build.output==output).first_or_404()

	return str(query.title())

