from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("site")

parser.add_argument("-c", "--connect", action="store_true")

args = parser.parse_args()

print(args)

print(args.site)

print(args.connect)
