export name=Exercise_1_Getting_Started
export header=_header.txt
for cluster in cees sherlock
do
	mkdir $name
	cp *py $name/
	## scripts to need header
	for script in run_cluster.py run_sp.py run_surf.py bulk_metal.py
	do
		rm $name/$script
		cat ../../Scripts/$cluster$header $script >> $name/$script
	done
	chmod +x $name/*py
	
	mkdir $name/Bulk $name/Cluster $name/Surface
	mv $name/bulk_metal.py $name/run_sp.py $name/Bulk
	mv $name/setup_surf.py $name/run_surf.py $name/Surface
	mv $name/setup_cluster.py $name/run_cluster.py $name/Cluster
	
	tar -cvf exercise_1_$cluster.tar $name
	rm -r $name
done