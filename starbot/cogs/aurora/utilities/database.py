# pylint: disable=cyclic-import
import json
import sqlite3
import time
from datetime import datetime, timedelta

from discord import Guild
from starbot.core import data_manager

from .logger import logger
from .utils import (convert_timedelta_to_str, generate_dict,
                    get_next_case_number)


def connect() -> sqlite3.Connection:
    """Connects to the SQLite database, and returns a connection object."""
    try:
        connection = sqlite3.connect(
            database=data_manager.cog_data_path(raw_name="Aurora") / "aurora.db"
        )
        return connection

    except sqlite3.OperationalError as e:
        logger.error("Unable to access the SQLite database!\nError:\n%s", e.msg)
        raise ConnectionRefusedError(
            f"Unable to access the SQLite Database!\n{e.msg}"
        ) from e


async def create_guild_table(guild: Guild):
    database = connect()
    cursor = database.cursor()

    try:
        cursor.execute(f"SELECT * FROM `moderation_{guild.id}`")
        logger.debug("SQLite Table exists for server %s (%s)", guild.name, guild.id)

    except sqlite3.OperationalError:
        query = f"""
            CREATE TABLE `moderation_{guild.id}` (
                moderation_id INTEGER PRIMARY KEY,
                timestamp INTEGER NOT NULL,
                moderation_type TEXT NOT NULL,
                target_type TEXT NOT NULL,
                target_id TEXT NOT NULL,
                moderator_id TEXT NOT NULL,
                role_id TEXT,
                duration TEXT,
                end_timestamp INTEGER,
                reason TEXT,
                resolved INTEGER NOT NULL,
                resolved_by TEXT,
                resolve_reason TEXT,
                expired INTEGER NOT NULL,
                changes TEXT NOT NULL,
                metadata TEXT NOT NULL
            )
        """
        cursor.execute(query)

        index_query_1 = f"CREATE INDEX IF NOT EXISTS idx_target_id ON moderation_{guild.id}(target_id);"
        cursor.execute(index_query_1)

        index_query_2 = f"CREATE INDEX IF NOT EXISTS idx_moderator_id ON moderation_{guild.id}(moderator_id);"
        cursor.execute(index_query_2)

        index_query_3 = f"CREATE INDEX IF NOT EXISTS idx_moderation_id ON moderation_{guild.id}(moderation_id);"
        cursor.execute(index_query_3)

        insert_query = f"""
            INSERT INTO `moderation_{guild.id}`
            (moderation_id, timestamp, moderation_type, target_type, target_id, moderator_id, role_id, duration, end_timestamp, reason, resolved, resolved_by, resolve_reason, expired, changes, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        insert_values = (
            0,
            0,
            "NULL",
            "NULL",
            0,
            0,
            0,
            "NULL",
            0,
            "NULL",
            0,
            "NULL",
            "NULL",
            0,
            json.dumps([]),
            json.dumps({}),
        )
        cursor.execute(insert_query, insert_values)

        database.commit()

        logger.debug(
            "SQLite Table (moderation_%s) created for %s (%s)",
            guild.id,
            guild.name,
            guild.id,
        )

    database.close()


async def mysql_log(
    guild_id: str,
    author_id: str,
    moderation_type: str,
    target_type: str,
    target_id: int,
    role_id: int,
    duration: timedelta,
    reason: str,
    database: sqlite3.Connection = None,
    timestamp: int = None,
    resolved: bool = False,
    resolved_by: str = None,
    resolved_reason: str = None,
    expired: bool = None,
    changes: list = None,
    metadata: dict = None,
) -> int:
    if not timestamp:
        timestamp = int(time.time())

    if duration != "NULL":
        end_timedelta = datetime.fromtimestamp(timestamp) + duration
        end_timestamp = int(end_timedelta.timestamp())

        duration = convert_timedelta_to_str(duration)
    else:
        end_timestamp = 0

    if not expired:
        if int(time.time()) > end_timestamp:
            expired = 1
        else:
            expired = 0

    if resolved_by is None:
        resolved_by = "NULL"

    if resolved_reason is None:
        resolved_reason = "NULL"

    if not database:
        database = connect()
        close_db = True
    else:
        close_db = False
    cursor = database.cursor()

    moderation_id = await get_next_case_number(guild_id=guild_id, cursor=cursor)

    sql = f"INSERT INTO `moderation_{guild_id}` (moderation_id, timestamp, moderation_type, target_type, target_id, moderator_id, role_id, duration, end_timestamp, reason, resolved, resolved_by, resolve_reason, expired, changes, metadata) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    val = (
        moderation_id,
        timestamp,
        moderation_type,
        target_type,
        target_id,
        author_id,
        role_id,
        duration,
        end_timestamp,
        reason,
        int(resolved),
        resolved_by,
        resolved_reason,
        expired,
        json.dumps(changes if changes else []),
        json.dumps(metadata if metadata else {}),
    )
    cursor.execute(sql, val)

    cursor.close()
    database.commit()
    if close_db:
        database.close()

    logger.debug(
        "Row inserted into moderation_%s!\n%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",
        guild_id,
        moderation_id,
        timestamp,
        moderation_type,
        target_type,
        target_id,
        author_id,
        role_id,
        duration,
        end_timestamp,
        reason,
        int(resolved),
        resolved_by,
        resolved_reason,
        expired,
        changes,
        metadata,
    )

    return moderation_id


async def fetch_case(moderation_id: int, guild_id: str) -> dict:
    """This method fetches a case from the database and returns the case's dictionary."""
    database = connect()
    cursor = database.cursor()

    query = f"SELECT * FROM moderation_{guild_id} WHERE moderation_id = ?;"
    cursor.execute(query, (moderation_id,))
    result = cursor.fetchone()

    cursor.close()
    database.close()

    return generate_dict(result)
