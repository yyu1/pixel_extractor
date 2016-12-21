#point in amazon -67.97526,-2.87726
#pixel resolution 7.5sec





import numpy as np
import memmap_extraction

testfile = '/Volumes/Global_250m/output/v5.1/maxent_agb_global_v5.1_masked_latlon.flt'
datatype = np.float32

xdim = 172800
ydim = 86400

extract_rows=[44581,44582,44583,44583,44583]
extract_cols=[53771,53772,53773,53774,53775]

result = memmap_extraction.memmap_extraction(testfile, datatype, xdim, ydim, extract_rows, extract_cols)


print(result)


