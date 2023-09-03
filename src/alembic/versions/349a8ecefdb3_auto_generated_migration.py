"""Auto-generated migration

Revision ID: 349a8ecefdb3
Revises:
Create Date: 2023-09-01 18:31:39.657702

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "349a8ecefdb3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_user_email", table_name="user")
    op.drop_index("ix_user_id", table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "is_active", sa.BOOLEAN(), autoincrement=False, nullable=True
        ),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("created_by", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("updated_by", sa.UUID(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
    )
    op.create_index("ix_user_id", "user", ["id"], unique=False)
    op.create_index("ix_user_email", "user", ["email"], unique=False)
    # ### end Alembic commands ###