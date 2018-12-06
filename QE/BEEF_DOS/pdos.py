import cPickle as pickle
from ase import io
from espresso import espresso


atoms = io.read('relaxed.traj')
atoms.set_pbc((True,True,True))

kpts = (4,4,1)

# make sure these settings are consistent with what you have been using!
calc=espresso(pw=500,
              dw=5000,
              kpts=kpts,
              nbands=-20,
              sigma=0.1,
              xc='BEEF-vdW',
              psppath='/home/vossj/suncat/psp/gbrv1.5pbe',
              outdir='pdos',
              convergence = {'mixing':0.1,'maxsteps':200},
              output = {'avoidio':True,'removewf':True,'wf_collect':False},
              )

atoms.set_calculator(calc)
energy = atoms.get_potential_energy()
print 'energy:',energy


dos = calc.calc_pdos(nscf=True, kpts=kpts, tetrahedra=False, sigma=0.2)

#save dos and pdos into pickle file
f = open('out_dos.pickle', 'w')
pickle.dump(dos, f)
f.close()