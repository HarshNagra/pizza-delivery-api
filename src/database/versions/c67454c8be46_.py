""" create the Order and Item tables

Revision ID: c67454c8be46
Revises: 4f2e2c180af
Create Date: 2016-10-02 16:00:01.042947

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector
from models import MENU


# revision identifiers, used by Alembic.
revision = 'c67454c8be46'
down_revision = '4f2e2c180af'


def upgrade():
    # reference: https://stackoverflow.com/a/24623979
    op.create_table(
        'order',
        sa.Column('order_id', sa.String(length=300), nullable=False),
        sa.Column('items', sa.JSON(), nullable=False),
        sa.Column('delivery', sa.JSON(), nullable=True),
        sa.Column('total_price', sa.Float, nullable=True),
        sa.PrimaryKeyConstraint('order_id')
    )
    item = op.create_table(
        'item',
        sa.Column('item_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(300), nullable=False),
        sa.Column('price', sa.Float, nullable=True),
        sa.Column('size', sa.String(300), nullable=True),
        sa.Column('category', sa.String(300), nullable=True),
        sa.PrimaryKeyConstraint('item_id')
    )
    op.bulk_insert(
        item,
        MENU,
    )


def downgrade():
    # https://stackoverflow.com/a/55058566
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    for table_name in ['order', 'item']:
        if table_name in tables:
            op.drop_table(table_name)
