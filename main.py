# Copyright (c) 2020 brainlife.io
#
# Author: Amin Saberi

# set up environment
import json
import nilearn.image as nlimg

# load inputs from config.json
with open('config.json') as config_json:
	config = json.load(config_json)

# Load into variables predefined code inputs
in_filename = str(config['fmri'])
 
# Get the number of volumes to be removed
n_vols = int(config['n_vols'])

# Load the input fMRI image and remove the first n_vols volumes
in_func_img = nlimg.load_img(in_filename)
out_func_img = in_func_img.slicer[:,:,:,n_vols:]

# save the output file (with the new resolution) to disk
out_func_img.to_filename('out_dir/bold.nii.gz')

