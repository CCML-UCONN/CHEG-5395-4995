export name=Exercise_3_Transition_States
export header=_header.txt
for cluster in cees sherlock
do
	mkdir $name
	cp -r Gaseous_Molecules $name/
	cp *py $name/
	## scripts to need header
	for script in fbl.py neb.py neb_restart.py run_freq.py
	do
		rm $name/$script
		cat ../../Scripts/$cluster$header $script >> $name/$script
	done
	chmod +x $name/*py
	
	mkdir $name/NEB $name/FBL $name/Vibrations
	mv $name/neb*py $name/NEB
	mv $name/fbl.py $name/FBL
	mv $name/run_freq.py $name/get_gas_free_energy.py $name/get_ads_free_energy.py $name/Vibrations

	tar -cvf exercise_3_$cluster.tar $name
	rm -r $name
done