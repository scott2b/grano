from flask import Blueprint, render_template, request, Response
from flask import redirect, make_response

from grano.lib.serialisation import jsonify
from grano.lib.args import object_or_404
from grano.model import Project, Permission, Pipeline, LogEntry
from grano.lib.pager import Pager
from grano.core import app, db, url_for
from grano.views.cache import validate_cache
from grano import authz


blueprint = Blueprint('log_entries_api', __name__)


@blueprint.route('/api/1/pipelines/<pipeline_id>/log', methods=['GET'])
def index(pipeline_id):
    pipeline = object_or_404(Pipeline.by_id(pipeline_id))
    authz.require(authz.project_read(pipeline.project))

    query = LogEntry.all()
    query = query.filter(LogEntry.pipeline==pipeline)

    if request.args.get('level'):
        query = query.filter(LogEntry.level==request.args.get('level'))

    pager = Pager(query)
    validate_cache(keys=pager.cache_keys())
    return jsonify(pager, index=True)


@blueprint.route('/api/1/pipelines/<pipeline_id>/log/<id>', methods=['GET'])
def view(pipeline_id, id):
    pipeline = object_or_404(Pipeline.by_id(pipeline_id))
    authz.require(authz.project_read(pipeline.project))
    log_entry = object_or_404(LogEntry.by_id(id))
    return jsonify(log_entry)
