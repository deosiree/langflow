"""Merge represented audit identity and the current release migrations.

Revision ID: d8e9f0a1b2c3
Revises: b6c84e92a0f1, f4b8c1d2e3a6
Phase: EXPAND
"""

revision = "d8e9f0a1b2c3"  # pragma: allowlist secret
down_revision = ("b6c84e92a0f1", "f4b8c1d2e3a6")  # pragma: allowlist secret
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Join both published histories without changing schema or data."""


def downgrade() -> None:
    """Restore both revision heads without changing schema or data."""
