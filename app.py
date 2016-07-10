import argparse
import json
import logging

from groups.app import GroupingService

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__file__)
logging.basicConfig(format=LOG_FORMAT)


def main(num_groups, infile, outfile='groups.json'):
    logger.debug("Parsing file %s", infile)
    with open(infile) as f:
        geodata = json.load(f)

    svc = GroupingService(geodata)
    groupings = svc.group_by_proximity(num_groups=num_groups)
    print groupings
    return
    with open(outfile, 'w') as out:
        out.write(json.dumps(groupings))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("groupings", help="Number of groupings to generate.", type=int)
    parser.add_argument("filename", help="Filename of geodata in JSON format.")
    parser.add_argument("--debug", help="Debug mode", action="store_true")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    main(args.groupings, args.filename)
