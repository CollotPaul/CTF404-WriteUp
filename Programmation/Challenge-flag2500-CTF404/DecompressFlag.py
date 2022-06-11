import tarfile	
from pathlib import Path
import os

for i in range(2500):
	fname = "flag"+str(2500-i)+".tar.gz"
	path = Path(fname)
	print(fname,path.is_file())
	if(path.is_file()==False):
		fname = "flag"+str(2500-i)+".tar"
		path = Path(fname)
		print(fname,path.is_file())
		if(path.is_file()==False):
			fname = "flag"+str(2500-i)+".tar.xz"
			path = Path(fname)
			print(fname,path.is_file())
			if(path.is_file()==False):
				fname = "flag"+str(2500-i)+".tar.bz2"
				path = Path(fname)
				print(fname,path.is_file())
				if(path.is_file()==False):
					i-=2
	if fname.endswith("tar.gz"):
	    tar = tarfile.open(fname, "r:gz")
	    tar.extractall()
	    tar.close()
	elif fname.endswith("tar"):
	    tar = tarfile.open(fname, "r:")
	    tar.extractall()
	    tar.close()
	elif fname.endswith("tar.xz") or fname.endswith("tar.bz2"):
	    tar = tarfile.open(fname)
	    tar.extractall()
	    tar.close()
	os.remove(fname)
	