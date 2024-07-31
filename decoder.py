import flask_unsign

print(flask_unsign.sign({'username': 'Sam'}, secret="CHANGEME"))