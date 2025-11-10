thonimport asyncio

async def async_sleep(seconds: float):
    """Async wrapper around sleep."""
    await asyncio.sleep(seconds)