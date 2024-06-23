"""add psswd column to user

Revision ID: 89cb4ef18210
Revises: 0638fe0699bc
Create Date: 2024-06-21 16:05:29.839823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89cb4ef18210'
down_revision: Union[str, None] = '0638fe0699bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
