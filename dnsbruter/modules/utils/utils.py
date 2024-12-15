from dnsbruter.modules.logger.logger import logger
import aiofiles
import os

async def Return_reader(file: str) -> list[str]:
    try:
        content = []
        async with aiofiles.open(file, "r") as streamr:
            data = await streamr.read()
            data = data.splitlines()
        for d in data:
            content.append(d)
        return content
    except PermissionError:
        logger(f"{file} have insufficient permission to read", "warn")
    except FileNotFoundError:
        logger(f"{file}: no such file or directory exist", "error")
        exit(1)
    except Exception as e:
        logger(f"Exception occured in return reader due to: {e}, {type(e)}", "warn")
        exit(1)
        

async def check_perm(filename) -> bool:
    try:
        async with aiofiles.open(filename, mode='a') as file:
            pass
    except PermissionError:
        logger(f"{filename} have insufficient permission to write", "warn")
        exit(1)
    except Exception as e:
        logger(f"Exception occured in util permission checker due to: {e}, {type(e)}", "warn")
