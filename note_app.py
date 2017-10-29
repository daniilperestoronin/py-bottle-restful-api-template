from bottle import run
from controllers.note_controller import NoteController

note_controller = NoteController()

run(host='localhost', port=8070, debug=True)
