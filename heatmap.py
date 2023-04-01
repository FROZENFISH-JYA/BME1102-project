import seaborn as sns
import matplotlib.cm
sns.set(font_scale=1.5)

import matplotlib.image as mpimg 
map_img = mpimg.imread('map_shanghaitech.jpg') 

# making and plotting heatmap 
import numpy.random as random 
heatmap_data = random.rand(10,10) 

sns.set_context({"figure.figsize":(10,10)})
hmax = sns.heatmap(heatmap_data,
            #cmap = al_winter, # this worked but I didn't like it
            
            alpha = 0.2, # whole heatmap is translucent
            annot = False,
            zorder = 2,
            )

hmax.imshow(map_img,
          aspect = hmax.get_aspect(),
          extent = hmax.get_xlim() + hmax.get_ylim(),
          zorder = 1) #put the map under the heatmap

from matplotlib.pyplot import show 
show()
