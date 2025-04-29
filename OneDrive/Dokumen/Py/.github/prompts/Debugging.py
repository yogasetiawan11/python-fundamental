# start from import pdb

import pdb
 
def cloud_stack(z, x):
    result = z + x  
    pdb.set_trace() # set a trace / debugging
    return result

result = cloud_stack(3, 5) # enter value of z, x
print(result)
