"""cereate users

Revision ID: cd6922eb736c
Revises: d5d0da727150
Create Date: 2025-12-17 11:04:01.885969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd6922eb736c'
down_revision: Union[str, Sequence[str], None] = 'd5d0da727150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
