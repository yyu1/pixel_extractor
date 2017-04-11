import numpy as np
import memmap_extraction as me

infile = '/nobackupp6/nexprojects/CMS-ALOS/maxent/output/100m_v6/combined/global_maxent_agb_combined_v6.int'
csvfile = '/nobackup/yyu1/samples/agb_train_v6/maxent_train_agb_v6_afr_valid.csv'
outfile = '/u/yyu1/100m/validation/v6/maxent_validation_agb_v6_afr.csv'

datatype = np.int16

#pixsize = 3.0/60.0/60.0   #7.5 seconds in degrees
pixsize = np.float64(92.662543333333333)   #modis sinusoidal grid

xdim = 432000
ydim = 159600

glas = np.genfromtxt(csvfile, delimiter=',', skip_header=1, usecols=(1,2))
lats = glas[:,1]
lons = glas[:,0]

ULX = np.float64(20015109.36)
ULY = np.float64(8450777.6177)


columns = ((lons+ULX)/pixsize).astype(np.int32)
rows = ((ULY-lats)/pixsize).astype(np.int32)   #image starts at 76 degrees north

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
