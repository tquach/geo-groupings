import argparse
import json

import geogroups
import settings
from geogroups import geopoints
from geogroups.geopoints import Grouping


def main(k, infile, outfile=settings.OUTPUT_FILE):
    geogroups.configure(settings)

    points = geopoints.from_file(infile)
    grouping = Grouping(points)
    buckets = grouping.group_by_proximity(k)

    with open(outfile, 'w') as out:
        out.write(json.dumps([g for g in buckets.itervalues()]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("k", help="Number of groupings to generate.", type=int)
    parser.add_argument("filename", help="Filename of geodata in JSON format.")
    args = parser.parse_args()
    main(args.k, args.filename)
