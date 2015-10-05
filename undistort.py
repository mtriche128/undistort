
# author: Matthew Triche
# brief : undistorts an image

# -----------------------------------------------------------------------------
# import modules

import cv2
import json
import argparse
import numpy

# -----------------------------------------------------------------------------
# define main function

def main():
	# ----- parse arguments -----
	
	parse = argparse.ArgumentParser(description="Undistort an image.")
	parse.add_argument("param_json", help="json file containing camera parameters")
	parse.add_argument("img_in", help="file name of input image")
	parse.add_argument("img_out", help="file name of output imahe")

	args = parse.parse_args()
	param_json = args.param_json
	img_in     = args.img_in
	img_out    = args.img_out
	
	# ----- read param_json -----
	
	try:
		param_file = open(param_json,"r")
	except IOError:
		print("Error: Unable to open parameter file.")
		exit(1)
	else:
		params = json.load(param_file)
		param_file.close()
	
	# ----- read input image -----
	
	input_img = cv2.imread(img_in)
	
	#if not(input_img.IsOpened()):
	if input_img == None:
		print("Error: Unable to read input image.")
		exit(1)
	
	# ----- ouput run parameters -----
	
	print("Distortion Coefficients  : %s" % str(params["dist_coeff"]))
	print("Camera Matrix            : %s" % str(params["cam_mat"]))
	print("Input Image Filename     : %s" % img_in)
	print("Output Image Filename    : %s" % img_out)
	
	# ----- undistort image -----
	
	height = len(input_img[:,1])
	width  = len(input_img[1,:]) 
	output_img = numpy.matrix([])
	cam_mat = numpy.matrix([params["cam_mat"][0:3],params["cam_mat"][3:6],params["cam_mat"][6:9]])
	dist_coeff = numpy.matrix( params["dist_coeff"] )
	
	output_img = cv2.undistort(input_img, cam_mat, dist_coeff, output_img)
	cv2.imwrite(img_out,output_img)

# -----------------------------------------------------------------------------
# run script

if __name__ == '__main__':
	main()
