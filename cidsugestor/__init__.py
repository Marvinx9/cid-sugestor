from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cde4c4sa5d54r86wg4sad8f48r964'

from cidsugestor import routes