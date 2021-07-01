
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--target_file', '-tf', type=str,
                    help='predict file to convert')
parser.add_argument('--resolution', '-r', default="1920,1080", type=str,
                    help='image resolution ')	
args = parser.parse_args()

default_img_size = (1920, 1080)
target_img_size = tuple(map(int, args.resolution.split(",")))
assert default_img_size == target_img_size, "Wrong size, you should downscale your video or image to (1920,1080)"

print("Start convert predict file to gt format")
rows = []
with open(args.target_file, "rt") as f:
	for line in f:
		rows.append(line.strip().split(",")[:-1])

for i in range(len(rows)):
	rows[i][-2] = '1'
	rows[i][-1] = '1.0'

with open("results/gt.txt", "wt") as f:
	for row in rows:
		f.write(",".join(row) + "\n")

print("Finish convert")