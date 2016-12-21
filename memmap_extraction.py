import numpy as np

def memmap_extraction(inFileName, data_type, in_dim_x, in_dim_y, extract_rows, extract_columns):
	image_data = np.memmap(inFileName, dtype = data_type, mode = 'r', shape=(in_dim_y,in_dim_x))

	#sort extract coords by y first and then x, because we assume data is ordered in BIL.

	return image_data[extract_rows, extract_columns]
	
