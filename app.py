import argparse
import json

import geogroups
import settings

from geogroups import geopoints


def main(k, infile, outfile=settings.OUTPUT_FILE):
    geogroups.configure(settings)

    points = geopoints.from_file(infile)
    groupings = geopoints.group_by(points, k)

    x = [json.loads(g.as_json()) for g in groupings]
    with open(outfile, 'w') as out:
        out.write(json.dumps(x))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("groupings", help="Number of groupings to generate.", type=int)
    parser.add_argument("filename", help="Filename of geodata in JSON format.")
    args = parser.parse_args()
    main(args.groupings, args.filename)
