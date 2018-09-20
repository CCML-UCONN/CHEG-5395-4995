export name=BEEF_DOS
export header=_header.txt
for cluster in cees sherlock
do
	mkdir $name
	cp *py $name/
	## scripts to need header
	for script in error_est.py pdos.py
	do
		rm $name/$script
		cat ../../Scripts/$cluster$header $script >> $name/$script
	done
	chmod +x $name/*py

	tar -cvf beef_dos_$cluster.tar $name
	rm -r $name
done