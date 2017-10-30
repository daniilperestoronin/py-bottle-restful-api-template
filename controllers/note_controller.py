from bottle import route


@route('/notes/', method='POST')
def create():
    return "yes"


@route('/notes/<id_note>', method='GET')
def read(id_note):
    return "yes" + id_note


@route('/notes/', method='PUT')
def update():
    return "yes"


@route('/notes/<id_note>', method='DELETE')
def delete(id_note):
    return "yes" + id_note


@route('/notes/', method='GET')
def read_all():
    return "all"
