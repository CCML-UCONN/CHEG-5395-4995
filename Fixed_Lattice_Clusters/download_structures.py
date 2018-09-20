import os

cluster_path = '/scratch/users/ctsai89/CHE444/2016/cluster_fixed_benchmark'
systems = open('systems.txt').readlines()
os.system('ssh-keygen -R sherlock.stanford.edu')
for system in systems:
    try:
        elements = system.strip()
        os.system('scp ctsai89@sherlock.stanford.edu:'+cluster_path+'/Fixed_opt_lattice/'+elements+'.traj .')

    except:
        print system+' not optimized'
