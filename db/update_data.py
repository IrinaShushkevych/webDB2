from db import session, Groups, Gradebook, Students, Subjects, Teachers

def insert_teacher(name):
    t = Teachers(teacher_name = name)
    session.add(t)
    session.commit()

def update_teacher(id, name):
    pass