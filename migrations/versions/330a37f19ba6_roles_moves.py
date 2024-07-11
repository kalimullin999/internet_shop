"""roles moves

Revision ID: 330a37f19ba6
Revises: 12718e0b228d
Create Date: 2024-06-11 15:52:52.219736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '330a37f19ba6'
down_revision: Union[str, None] = '12718e0b228d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'users', 'roles', ['role'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.alter_column('users', 'role',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
