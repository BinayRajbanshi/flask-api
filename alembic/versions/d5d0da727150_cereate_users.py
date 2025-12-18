"""cereate users

Revision ID: d5d0da727150
Revises: 4617f263ec3e
Create Date: 2025-12-17 11:03:12.490153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5d0da727150'
down_revision: Union[str, Sequence[str], None] = '4617f263ec3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
