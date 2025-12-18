"""modified user table

Revision ID: e8645b8e481f
Revises: cd6922eb736c
Create Date: 2025-12-17 11:26:20.528913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8645b8e481f'
down_revision: Union[str, Sequence[str], None] = 'cd6922eb736c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
