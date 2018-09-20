export name=All_scripts
export header=_header.txt
for cluster in cees sherlock
do
	mkdir $name
	cp ../ASE/Getting_Started/setup_surf.py ../ASE/Getting_Started/setup_cluster.py ../ASE/Adsorption/setup_ads.py ../ASE/BEEF_DOS/error_est.py $name/
	mkdir temp
	cp ../ASE/Getting_Started/bulk_metal.py ../ASE/Adsorption/opt.py   ../ASE/Transition_States/fbl.py ../ASE/Transition_States/run_freq.py  ../ASE/BEEF_DOS/pdos.py temp/
	## scripts that need header
	for script in bulk_metal.py opt.py fbl.py run_freq.py pdos.py
	do
		cat $cluster$header temp/$script >> $name/$script
	done
	rm temp/*
	rmdir temp
	chmod +x $name/*py
	
	tar -cvf all_$cluster.tar $name
	rm -r $name
done