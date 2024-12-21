import aiohttp


async def get_status(host: str, port: int = 25565) -> tuple[bool, dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.mcsrvstat.us/2/{host}:{port}') as response:
            response = await response.json()
            if response['online']:
                return (True, response)
            return (False, response)
