[![Build Status](https://travis-ci.org/tquach/geo-groupings.svg?branch=master)](https://travis-ci.org/tquach/geo-groupings)

# Geo Point Groupings

This implementation generates a series of groupings for a given set of geodata locations based on proximity.

# Installing

	pip install -r requirements.txt

# Running

	python app.py <num_partitions> <path/to/json_data_file>

# Background

This implementation uses a k-means partitioning approach from the sklearn library. There is an alternate approach
which uses DBSCAN which is similar to the k-means approach, but
