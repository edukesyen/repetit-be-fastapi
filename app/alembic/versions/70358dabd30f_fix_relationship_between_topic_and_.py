"""fix relationship between topic and flashcard

Revision ID: 70358dabd30f
Revises: 8b32af67e990
Create Date: 2024-06-19 10:10:53.302900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70358dabd30f'
down_revision: Union[str, None] = '8b32af67e990'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
