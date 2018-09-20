export CURDIR=$PWD                               #save current directory
for ads in 2N_surface 2N_cluster N NH NH2 NH3 H    #loop through first directory
do
for site in $ads/*/        #loop through ALL subdirectories of ads folder
    do                     #you can also specify individually or use wildcards
    # cp opt.py $site      #you can copy opt.py from CURDIR to the subdirs
    cd $site
        if [[ $HOSTNAME == *"sherlock"* ]]
        then
            sbatch --job-name=$PWD opt.py     #sbatch if sherlock
        else
            qsub opt.py                       #qsub if cees
        fi
        cd $CURDIR        #go back to the original directory and continue loop
    done
done