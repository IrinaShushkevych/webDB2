from sqlalchemy import select, func, desc

from models import Groups, Gradebook, Students, Subjects, Teachers
from connect import session

qparams = [
    [0, 0],
    [1, 2],
    [1, 1],
    [0, 0],
    [1, 1],
    [1, 1],
    [2, 1],
    [1, 1],
    [1, 1],
    [2, 1],
    [2, 1],
    [2, 2]
    ]

def q_1():
    res = []
    print(res)
    res = session.query(
            Students.student_name, 
            Groups.group_name, 
            func.round(func.avg(Gradebook.grade), 2).label('average_grade') )\
        .select_from(Gradebook)\
        .join(Students)\
        .join(Groups)\
        .group_by(Students.id, Groups.group_name)\
        .limit(5)\
        .all()
    print(res)
    return res


def q_2():

if __name__ == "__main__":
    print('MAin')
    q_1()
    q_2()




# """
# SELECT s.student_name, gr.group_name, IFNULL(SUM(g.grade)/COUNT(g.grade), 0) as avarage_grade 
# FROM  students s LEFT JOIN groups gr ON s.id_group = gr.id 
# 	LEFT JOIN gradebook g ON s.id = g.id_student 
# group by g.id_student 
# order by avarage_grade DESC, s.student_name 
# LIMIT 5
# """