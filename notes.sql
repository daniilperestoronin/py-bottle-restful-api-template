CREATE DATABASE notes;
CREATE USER notes_user WITH password 'order_user';
GRANT ALL ON DATABASE notes TO notes_user;

CREATE TABLE notes(
	id bigserial PRIMARY KEY,
	creation_date DATE NOT NULL,
  note_text TEXT NOT NULL);
