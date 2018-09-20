#!/usr/bin/env /home/vossj/suncat/bin/python
"""Script for submitting all files."""

import os

curdir = os.environ.get('PWD')
print 'Confirm submission for {curdir}: [y/n]'.format(curdir=curdir)
confirmation = raw_input()

if confirmation == 'y':
    print 'What is your system? (e.g. Ag, PtMo)'
    metal = raw_input()
    print 'Confirm that your system is {metal}? [y/n]'.format(metal=metal)
    confirm_metal = raw_input()
    if confirm_metal == 'y':
        hostname = os.environ.get('HOSTNAME')
        username = os.environ.get('USER')

        if 'cees' in hostname:
            destination = '/data/cees/cheme444/Results/'
            partition = '/data/cees/{username}'.format(username=username)
        elif 'sherlock' in hostname:
            destination = '/scratch/PI/suncat/chemeng444_2016/Results/'
            partition = os.environ.get('SCRATCH')

        os.system('chmod 755 {p}'.format(p=partition))
        os.system('chmod 755 {p}/*'.format(p=partition))
        if os.path.exists('{d}/{m}_{u}'.format(d=destination, m=metal, u=username)):
            os.system('rm {d}/{m}_{u}'.format(d=destination,
                                              m=metal,
                                              u=username))
        os.system(
            'ln -s {curdir} {destination}/{metal}_{username}'.format(c=curdir,
                                                                     d=destination,
                                                                     m=metal,
                                                                     u=username))
    else:
        exit()
else:
    exit()
