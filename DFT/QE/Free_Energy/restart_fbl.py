from ase.io import read, write
from glob import glob
import sys, os

trajnames = sorted(glob('i?.traj'))+sorted(glob('i??.traj'))
fbl_traj = [read(traj) for traj in trajnames if os.stat(traj).st_size != 0]
outname = sys.argv[1]
write(outname+'.traj', fbl_traj)