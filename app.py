from flask import Flask

from controller.student_controller import studente_bp
from controller.teacher_controller import docente_bp
from controller.course_controller import corso_bp

app = Flask(__name__)

app.register_blueprint(studente_bp)
app.register_blueprint(docente_bp)
app.register_blueprint(corso_bp)

# La 5000 è la default
if __name__ == "__main__":
    app.run(debug=True, port=5000)
