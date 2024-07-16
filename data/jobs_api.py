from datetime import datetime

import flask
from flask import jsonify, make_response, request
from sqlalchemy import DateTime

from . import db_session
from . jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    jobs_list = [
        {
            "id": job.id,
            "user_id": job.user_id,
            "job": job.job,
            "work_size": job.work_size,
            "collaborators": job.collaborators,
            "start_date": job.start_date,
            "end_date": job.end_date,
            "is_finished": job.is_finished
        }
        for job in jobs
    ]
    return jsonify(jobs_list)


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'user_id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['user_id', 'job', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        user_id=request.json['user_id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)

    data = request.json
    if not data:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    if 'job' in data:
        job.job = data['job']
    if 'work_size' in data:
        job.work_size = data['work_size']
    if 'user_id' in data:
        job.user_id = data['user_id']
    if 'collaborators' in data:
        job.collaborators = data['collaborators']
    if 'start_date' in data:
        job.start_date = datetime.fromisoformat(data['start_date'])
    if 'end_date' in data:
        job.end_date = datetime.fromisoformat(data['end_date'])
    if 'is_finished' in data:
        job.is_finished = data['is_finished']

    db_sess.commit()
    return jsonify({'success': 'OK'})
