"""
Constants specific to PostgreSQL.
"""

# The maximum length of an identifier is 63 by default, but can be
# changed by recompiling PostgreSQL after editing the NAMEDATALEN
# macro in src/include/pg_config_manual.h.
IDENTIFIER_MAX_LENGTH = 63
