#!/usr/bin/env python

import argparse

def arg_parser():
	parser = argparse.ArgumentParser(description="My first argument parser")
	parser.add_argument("name", help="Name of person to greet.")
	return(parser.parse_args())

args = arg_parser()
greeting = "Greetings, {}!".format(args.name)
print(greeting)