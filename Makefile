cacheSim:	
	echo "#!/bin/bash" > cacheSim
	echo "python3 cacheSim.py \"\$$@\"" >> cacheSim
	chmod u+x cacheSim