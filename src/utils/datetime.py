from datetime import datetime, timedelta

DEFAULT_DATETIME_TEMPLATE = '%d.%m.%Y %H:%M'
DEFAULT_DATE_TEMPLATE = '%d.%m.%Y'


def parse_datetime(
        date_iso8601: str,
        *,
        present: bool = False,
        limit: timedelta = None,
) -> datetime:
    date = datetime.fromisoformat(date_iso8601.replace('Z', '+00:00'))  # support for Zulu time
    now = datetime.now()
    if present and limit is not None:
        raise AttributeError("Cannot use args 'present' and 'limit' together")
    if present:
        assert date > now
    if limit is not None:
        assert date > now + limit
    return date


def is_date(string: str) -> bool:
    try:
        datetime.strptime(string, DEFAULT_DATE_TEMPLATE)
        return True
    except ValueError:
        return False
