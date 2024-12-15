import argparse
from dnsbruter.modules.logger.logger import logger

def cli():
    try:
        parser =  argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False )
        parser.add_argument("-h", "--help", action="store_true")
        parser.add_argument("-d", "--domain", type=str)
        parser.add_argument("-dL", "--domain-list", type=str)
        parser.add_argument("-w", "--wordlist", type=str)
        parser.add_argument("-c", "--concurrency", type=int, default=100)
        parser.add_argument("-up", "--update", action="store_true")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("-s", "--silent", action="store_true")
        parser.add_argument("-o", "--output", type=str)
        parser.add_argument("-j", "--json", action="store_true")
        parser.add_argument("-duc", "--disable-check", action="store_true")
        parser.add_argument("-rl", "--resolver", type=str)
        parser.add_argument("-wd", "--wildcard-detect", action="store_true")
        parser.add_argument("-wt", "--wildcard-threads", type=int, default=20)
        parser.add_argument("-wrt", "--wildcard-ratelimit", type=int, default=2000)
        parser.add_argument("-ov", "--override", action="store_true")
        parser.add_argument("-ws", "--wildcard-output", type=str)
        parser.add_argument("-sd", "--sec-deb", action="store_true")
        parser.add_argument("-rt", "---rate-limit", type=int, default=2000)
        parser.add_argument("-dl", "--delay", type=int, default=1)
        return parser.parse_args()
    except argparse.ArgumentError as e:
        logger("Please use the command for more infromation: dnsbruter -h")
        quit()
    except argparse.ArgumentTypeError as e:
        logger("Please use the command for more infromation: dnsbruter -h")
        quit()
    except KeyboardInterrupt as e:
        logger("CTRL+C Pressed", "warn")
    except Exception as e:
        pass