import secrets


async def generate_unique_id(k: int = 64):
    unique_id = secrets.randbits(k)
    while await database.by("users").find({"unique_id": unique_id}) is not None:
        unique_id = secrets.randbits(k)

    return unique_id
