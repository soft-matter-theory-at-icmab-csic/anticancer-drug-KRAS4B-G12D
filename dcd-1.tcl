package require psfgen
package require molefacture
package require alchemify
package require readcharmmtop
package require pbctools

resetpsf
pdbalias residue HIS HSD
pdbalias atom ILE CD1 CD

#topology /data/mabuyong/src/charmm/martini/top_all27_prot_lipid_na.inp

mol new ../../step5_input.psf
#mol addfile ../../ionized-center.pdb
#for {set j 1} {$j < 3} {incr j} {
 for {set i 51} {$i <= 300} {incr i} {
#mol addfile ../run$j/abeta-prun$i.dcd step 1 type  dcd step 1    waitfor all
 mol addfile ../step7_$i.nc step 5 type  netcdf  step 5  waitfor all
#  mol addfile ../abeta-prun$i.dcd  type  dcd  waitfor all
       }
#          }

                        pbc unwrap -all -sel "all not water"

 set num_steps [molinfo top get numframes]
# set num_steps [expr ($num_steps - 1)]


#write dcd file for protein only
 for {set frame 0} {$frame < $num_steps} {incr frame} {
   # add new frame to the trajectory, with coords copied from previous frame
   animate dup frame $frame 0
   incr frame
   animate goto $frame
   # modify coords of new frame
   #(do your own thing here)
}
# write the complete trajectory to disk
animate write dcd chainPH-deletefirst500ns.dcd beg 0 end $num_steps skip 1 sel [atomselect top "chain P H"]
animate write dcd chainP-deletefirst500ns.dcd beg 0 end $num_steps skip 1 sel [atomselect top "chain P"]
#animate write dcd protein-dry.dcd beg 0 end $num_steps skip 1 sel [atomselect top "segid PROA PROB PROC PROD PROE "]
#write file_type filename [beg nb] [end ne ] [skip ns] [waitfor nw] [sel selection] [molecule_number]

exit
