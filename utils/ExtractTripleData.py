#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np

pdb_data_small = pd.read_csv('pdbbind_core_df.csv')
pdb_proteinName_small = np.array(pdb_data_small['pdb_id'])
pdb_affinity_small = np.array(pdb_data_small['label'])
pdb_ligandName_small = np.array(pdb_data_small['smiles'])

f = open("pdbbind_core_df_cleaned.csv", "w")
f.write("proteinName,smiles,affinity,ligandName\n")
for i in range(len(pdb_data_small)):
    f.write("%s,%.2f,%s\n" % (pdb_proteinName_small[i], pdb_affinity_small[i], pdb_ligandName_small[i]))
f.close()


# In[ ]:




