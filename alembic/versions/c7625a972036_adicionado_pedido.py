"""Adicionado Pedido

Revision ID: c7625a972036
Revises: 3aa30891201c
Create Date: 2023-08-24 16:56:15.662525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7625a972036'
down_revision: Union[str, None] = '3aa30891201c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('localDeEntrega', sa.String(), nullable=True),
    sa.Column('tipoDeEntrega', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_pedido_produto'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_pedido_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pedido_id'), 'pedido', ['id'], unique=False)
    op.add_column('produto', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.drop_constraint('fk_usuario', 'produto', type_='foreignkey')
    op.create_foreign_key('fk_usuario', 'produto', 'usuario', ['usuario_id'], ['id'])
    op.drop_column('produto', 'usuario_Id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('usuario_Id', sa.INTEGER(), nullable=True))
    op.drop_constraint('fk_usuario', 'produto', type_='foreignkey')
    op.create_foreign_key('fk_usuario', 'produto', 'usuario', ['usuario_Id'], ['id'])
    op.drop_column('produto', 'usuario_id')
    op.drop_index(op.f('ix_pedido_id'), table_name='pedido')
    op.drop_table('pedido')
    # ### end Alembic commands ###
