"""Init

Revision ID: 7c1f5c328830
Revises: 
Create Date: 2022-12-30 19:34:00.763762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c1f5c328830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=150), nullable=False),
    sa.Column('id_group', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_group'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(length=150), nullable=False),
    sa.Column('id_teacher', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_teacher'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gradebook',
    sa.Column('id_student', sa.Integer(), nullable=False),
    sa.Column('id_subject', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['id_student'], ['students.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_subject'], ['subjects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_student', 'id_subject', 'createdAt')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gradebook')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('groups')
    # ### end Alembic commands ###
