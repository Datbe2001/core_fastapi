"""create user table

Revision ID: 554246ddc8ab
Revises: 
Create Date: 2023-11-13 15:02:48.081973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '554246ddc8ab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.String(length=255), nullable=False),
                    sa.Column('username', sa.String(length=255), nullable=False),
                    sa.Column('full_name', sa.String(length=255), nullable=True),
                    sa.Column('phone', sa.String(length=255), nullable=True),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('user')