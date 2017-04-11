import numpy as np
import memmap_extraction as me

infile = '/nobackupp6/nexprojects/CMS-ALOS/srtm1sec_mosaic/global_srtm3_aster_maxdegreeslope_3sec.byt'
csvfile = '/nobackupp6/nexprojects/CMS-ALOS/glas/global_glas_2003_2008_alltypes_formatted_agb_v6_srtmstdev.csv'
outfile = '/nobackupp6/nexprojects/CMS-ALOS/glas/global_glas_2003_2008_alltypes_formatted_agb_v6_srtmstdev_maxslope.csv'
#csvfile = '/nobackupp6/nexprojects/CMS-ALOS/glas/test.csv'
#outfile = '/nobackupp6/nexprojects/CMS-ALOS/glas/test_output.csv'

datatype = np.uint8

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
		output.write(header[:-1]+',\'srtm_maxslope\'\n')

		index = 0
		for line in input:
<<<<<<< HEAD
			print(extraction_values[index])
			output.write(line+','+str(extraction_values[index]))
=======
			output.write(line[:-1]+','+str(extraction_values[index])+'\n')
>>>>>>> d4433bb73ab32906796842a4e570e35cef73a165
			index = index + 1
