import aiofiles
from dnsbruter.modules.logger.logger import logger
import json

async def save(filename: str, content: str, Json: bool) -> None:
    try:
        async with aiofiles.open(filename, "a") as streamw:
            if Json:
                await streamw.write(json.dumps(content, indent=4)+ "\n")
            else:
                await streamw.write(content + '\n')
    except Exception as e:
        logger(f"Excpetion occured in the save module due to: {e}, {type(e)}, {content}", "warn")