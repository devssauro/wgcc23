"""initial table

Revision ID: 6e9e5cd91844
Revises:
Create Date: 2023-04-07 16:00:01.848714

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "6e9e5cd91844"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "opened_email",
        sa.Column("mandrill_id", sa.String(), nullable=True),
        sa.Column("mandrill_ip", sa.String(), nullable=True),
        sa.Column("mandrill_ts", sa.Integer(), nullable=True),
        sa.Column("location", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("user_agent", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("subject", sa.String(), nullable=True),
        sa.Column("recipient_email", sa.String(), nullable=True),
        sa.Column("sender_email", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=True),
        sa.Column("date_created", sa.DateTime(), nullable=True),
        sa.Column("date_modified", sa.DateTime(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("opened_email")
    # ### end Alembic commands ###
