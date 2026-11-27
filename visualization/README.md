# Reading the scale diagram

Each node represents one finite core disk. Its two children are the two strictly smaller cores inside it. The two horizontal coordinates separate addresses and generations. The extra vertical coordinate records the exact cumulative scale at that generation. The radii and separations are schematic.

Follow a single infinite binary address. The even cores have scalar 1 and the odd cores have scalar 2. In the mathematical construction, the quotient between the image displacement and the vertical step differs from the scalar times the vertical unit vector by at most 2^(−n−8). Consequently its two limits differ at every Cantor point. Direction errors still tend to zero uniformly on small cores, which explains how regular image tangents survive.

Extract the explorer ZIP and open index.html in a browser. The rotation, depth, and binary address controls run offline. The rotating GIF shows four levels. Regenerate the GIF with Python 3 and Pillow using the included render.py.
