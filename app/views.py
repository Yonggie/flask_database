from flask import Blueprint
from flask import request,Response,render_template,url_for,redirect,session
from app.ext import db
from .models import User
from random import randint

bp=Blueprint('bp',__name__)

def init_blue(app):
    app.register_blueprint(blueprint=bp)


@bp.route('/' ,methods=['GET','POST'])
def index():
    if request.method=='GET':
        infos=User.query.all()
        return render_template('index.htm',infos=infos)
    elif request.method=='POST':
        id=request.form.get('id')
        name = request.form.get('name')
        task=request.form.get('task')
        # we use the simplest function get.
        if task=='alter':
            user=User.query.get(id)
            user.name=name
            db.session.commit()
        elif task=='insert':
            user=User()
            user.id=id
            user.name=name
            db.session.add(user)
            db.session.commit()
        elif task=='delete':
            user=User.query.get(id)
            db.session.delete(user)
            db.session.commit()

        infos = User.query.all()
        return render_template('index.htm', infos=infos)

@bp.route('/alter/',methods=['GET'])
def alter():
    return render_template('alter.htm')

@bp.route('/insert/',methods=['GET'])
def insert():
    return render_template('insert.htm')

@bp.route('/delete/',methods=['GET'])
def delete():
    return render_template('delete.htm')

