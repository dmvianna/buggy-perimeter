#!/usr/bin/env python

"""
read a list of points from a CSV file and print out the length of the perimiter of the shape that is formed by joining the points in their listed order
"""

import csv
import sys


def perimeter(points):
    """ returns the length of the perimiter of some shape defined by a list of points """
    return sum(get_distances(points))


def get_distances(points):
    """ convert a list of points into a list of distances """
    if len(points) < 3:
        raise ValueError("Not a polygon: less than 3 vertices.")

    # I could have used a generator here, but I'm going for
    # readability rather than speed.
    def go(points_, acc=[]):
        if len(points_) == 1:
            acc.append(get_distance(points[0], points_[0]))
            return acc
        else:
            point = points_[0]
            next_point = points_[1]
            acc.append(get_distance(point, next_point))
            return go(points_[1:], acc)
        
    return go(points)


def get_distance(point1, point2):
    """ use pythagorean theorem to find distance between 2 points """
    a = (point1['x'] - point2['x']) ** 2
    b = (point1['y'] - point2['y']) ** 2
    return (a + b) ** (1.0 / 2)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    with open(sys.argv[1]) as fp:
        reader = csv.reader(fp)
        header = next(reader)
        points = []
        for row in [r for r in reader]:
            point = {}
            for i in range(len(header)):
                point[header[i]] = float(row[i])
            points.append(point)

        print perimeter(points)


if __name__ == "__main__":
    main()
