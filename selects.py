from sqlalchemy import select, func, and_

from models import Groups, Gradebook, Students, Subjects, Teachers
from connect import session

def res_to_dict(res):
    return [r._asdict() for r in res]

def print_res(res):
    if len(res) > 0:
        title = [key for key, value in res[0].items()]
    length_col = 30
    length = length_col * len(title) + 4
    print('-' * length)
    print_string = '|'
    for _ in title:
        print_string += ' {:^' + str(length_col - 2) + '} |'
    print(print_string.format(*title))
    print('-' * length)
    for el in res:
        print(print_string.format(*[str(value) for key, value in el.items()]))
        print('-' * length)
    print_string = '| {:<' + str(length - 4) + '} |'
    print(print_string.format(f'Row: {len(res)}'))
    print('-' * length)

def select_1():
    # 5 студентів з найбільшим середнім балом з усіх предметів
    sql = session.query(
            Students.student_name, 
            Groups.group_name, 
            func.round(func.avg(Gradebook.grade), 2).label('average_grade') )\
        .join(Gradebook)\
        .join(Groups)\
        .group_by(Students.id, Groups.group_name)\
        .limit(5)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_2(subject):
    # Студенти з найвищим середнім балом з певного предмету
    subsql = session.query(Gradebook.id_student, func.round(func.avg(Gradebook.grade), 2).label('grade'))\
             .filter(Gradebook.id_subject == subject)\
             .group_by(Gradebook.id_student)\
             .subquery()
    
    subq = session.query(func.max(subsql.c.grade).label('grade'))\
            .scalar_subquery()
    
    sub_from = session.query(subsql.c.id_student, subsql.c.grade)\
                .filter(subsql.c.grade == subq)\
                .subquery()
    
    sql = session.query(Students.student_name, Groups.group_name, sub_from.c.grade)\
            .join(Groups)\
            .join(sub_from, sub_from.c.id_student == Students.id)\
            .order_by(Students.student_name)
    
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_3(subject):
    # Середній бал у групах з певнjого предмету
    sql = session.query(Groups.group_name, func.round(func.avg(Gradebook.grade), 2).label('average_grade'))\
            .select_from(Gradebook)\
            .join(Students)\
            .join(Groups)\
            .filter(Gradebook.id_subject == subject)\
            .group_by(Groups.group_name)\
            .order_by(Groups.group_name)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_4():
    # Середній бал на потоці (по всіх)
    sql = session.query(func.round(func.avg(Gradebook.grade), 2).label('average_grade'))
    res = sql.scalar()
    print(res)
    return res

def select_5(teacher):
    # Курси певного викладача
    sql = session.query(Subjects.subject_name)\
            .filter(Subjects.id_teacher == teacher)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_6(group):
    # Список студентів певної групи
    sql = session.query(Students.student_name)\
            .filter(Students.id_group == group)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_7(group, subject):
    # Оцінки студентів у окремій группі з певного предмету
    sql = session.query(Gradebook.createdAt.label('grade_date'), Students.student_name, Gradebook.grade)\
            .join(Students)\
            .filter(and_(
                (Students.id_group == group),
                (Gradebook.id_subject == subject)))\
            .order_by(Gradebook.createdAt, Students.student_name)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_8(teacher):
    # Середній бал, який ставив певний викладач зі своїх предметів
    sql = session.query(Subjects.subject_name, func.round(func.avg(Gradebook.grade), 2).label('average_grade'))\
            .join(Gradebook)\
            .filter(Subjects.id_teacher == teacher)\
            .group_by(Subjects.subject_name)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_9(student):
    # Список курсів, які відвідував студент
    sql = session.query(Subjects.subject_name)\
            .join(Gradebook)\
            .filter(Gradebook.id_student == student)\
            .group_by(Subjects.subject_name)\
            .order_by(Subjects.subject_name)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_10(student, teacher):
    # Список курсів, які певний викладач читає певному студенту
    sql = session.query(Subjects.subject_name)\
            .join(Gradebook)\
            .filter(and_(
                (Gradebook.id_student == student),
                (Subjects.id_teacher == teacher)
            ))\
            .group_by(Subjects.subject_name)\
            .order_by(Subjects.subject_name)
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

def select_11(student, teacher):
    # Середній бал, який певний викладач ставить певному студенту
    sql = session.query(func.round(func.avg(Gradebook.grade), 2).label('average_grade'))\
            .join(Subjects)\
            .filter(and_(
                (Gradebook.id_student == student),
                (Subjects.id_teacher == teacher)
            ))
    res = sql.scalar()
    print(res)
    return res

def select_12(group, subject):
    # Оцінки студентів у певній групі з певного предмету на останньому занятті
    subq = session.query(func.max(Gradebook.createdAt))\
            .join(Students)\
            .filter(and_(
                (Students.id_group == group),
                (Gradebook.id_subject == subject)
            ))\
            .scalar_subquery()
    sql = session.query(Gradebook.createdAt.label('grade_date'), Students.student_name, Gradebook.grade)\
            .join(Students)\
            .filter(and_(
                (Students.id_group == group),
                (Gradebook.id_subject == subject),
                (Gradebook.createdAt == subq)
            ))
    res = sql.all()
    print_res(res_to_dict(res))
    return res_to_dict(res)

if __name__ == "__main__":
    print('--- Main ---')
    # select_1()
    # select_2(6)
    # select_3(3)
    # select_4()
    # select_5(1)
    # select_6(1)
    # select_7(1, 1)
    # select_8(3)
    # select_9(1)
    # select_10(1, 2)
    # select_11(1, 2)
    select_12(1, 2)