import argparse
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
 
from application.quart_app_factory import create_app

test_config = Config()
test_config.bind = ["localhost:5002"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', help='Use database', action='store_true')

    args, unknown = parser.parse_known_args()

    if unknown:
        print('ERROR : Uknown arguments : ', unknown)
    else:
        app = create_app(use_db=args.db)
        asyncio.run( serve(app, test_config) )

if __name__ == "__main__":
    main()
