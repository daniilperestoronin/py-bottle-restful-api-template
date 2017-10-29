from bottle import route


class NoteController(object):
    @route('/notes/', method='POST')
    def create(note):
        return "yes"

    @route('/notes/<id_note>', method='GET')
    def read(id_note):
        return "yes" + id_note

    @route('/notes/', method='PUT')
    def update(note):
        return "yes"

    @route('/notes/<id_note>', method='DELETE')
    def delete(id_note):
        return "yes" + id_note

    @route('/notes/', method='GET')
    def read_all():
        return "all"
