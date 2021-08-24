import os, random
import numpy as np
import shutil

files = os.listdir('rgb/')
sample = random.sample(files,2500)
# print(sample)

sample_np=np.array(sample)
np.save('selected_sim.npy',sample_np)

# img_list=np.load(‘selected_sim.npy’)
# img_list=img_list.tolist()


for name in sample:
  shutil.copy('rgb/'+name,'trainB/'+name)