export name=Exercise_2_Adsorption
export header=_header.txt
for cluster in cees sherlock
do
	mkdir $name
	cp *py $name/
	## scripts to need header
	for script in opt.py run_N2.py
	do
		rm $name/$script
		cat ../../Scripts/$cluster$header $script >> $name/$script
	done
	chmod +x $name/*py
	mkdir $name/Adsorbates $name/N2_gas 
	mv $name/opt.py $name/setup_ads.py $name/Adsorbates
	mv $name/run_N2.py $name/N2_gas
	
	tar -cvf exercise_2_$cluster.tar $name
	rm -r $name
done