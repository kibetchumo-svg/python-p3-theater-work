from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'create_roles_auditions'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('character_name', sa.String, nullable=False)
    )

    op.create_table(
        'auditions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('actor', sa.String, nullable=False),
        sa.Column('location', sa.String, nullable=False),
        sa.Column('phone', sa.Integer),
        sa.Column('hired', sa.Boolean, default=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id'))
    )


def downgrade():
    op.drop_table('auditions')
    op.drop_table('roles')
