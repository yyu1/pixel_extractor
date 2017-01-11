import numpy as np
import memmap_extraction as me

infile = '/nobackupp6/nexprojects/CMS-ALOS/srtm1sec_mosaic/global_srtm3_aster_stdev_3sec.int'
csvfile = '/u/yyu1/allometry_data_input/global_glas_2003_2008_alltypes_formatted_agb_v6.csv'
outfile = '/u/yyu1/allometry_data_input/global_glas_2003_2008_alltypes_formatted_agb_v6_srtmstdev.csv'

datatype = np.int16

pixsize = 3.0/60.0/60.0   #7.5 seconds in degrees

xdim = 432000
ydim = 158400

glas = np.genfromtxt(csvfile, delimiter=',', skip_header=1, usecols=(5,6))
lats = glas[:,0]
lons = glas[:,1]

columns = ((lons+180)/pixsize).astype(np.int32)
rows = ((76-lats)/pixsize).astype(np.int32)   #image starts at 76 degrees north

extraction_values = me.memmap_extraction(infile, datatype, xdim, ydim, rows, columns)

#Read lines of input csv and append the extracted values
with open(outfile, 'w') as output:
	with open(csvfile) as input:
		header = next(input)
		output.write(header+',\'srtm_stdev\'')

		index = 0
		for line in input:
			output.write(line+','+str(extraction_values[index]))
			index = index + 1
