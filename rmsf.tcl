package require psfgen
package require molefacture
package require alchemify
package require readcharmmtop
package require pbctools

resetpsf
pdbalias residue HIS HSD
pdbalias atom ILE CD1 CD

#topology /spin1/users/mabuyong/src/charmm/martini/top_all27_prot_lipid_na.inp

mol new ../dcd/protein.psf
mol addfile ../dcd/protein.pdb
mol addfile ../dcd/chainP-deletefirst500ns.dcd type dcd waitfor all
#for {set j 2} {$j < 10} {incr j} {
# for {set i 1} {$i < 61} {incr i} {
# mol addfile ../run$j/abeta-prun$i.dcd step 1 type  dcd step 1    waitfor all
#  mol addfile ../abeta-prun$i.dcd  type  dcd  waitfor all
#       }
#          }

#                        pbc unwrap -all -sel "all not water"

 set num_steps [molinfo top get numframes]
 set num_steps [expr ($num_steps - 1)]


#write dcd file for protein only
# for {set frame 0} {$frame < $num_steps} {incr frame} {
#   # add new frame to the trajectory, with coords copied from previous frame
#   animate dup frame $frame 0
#   incr frame
#   animate goto $frame
   # modify coords of new frame
   #(do your own thing here)
#}
# write the complete trajectory to disk
#animate write dcd protein-dry.dcd beg 0 end $num_steps skip 1 sel [atomselect top "segid PROA PROB PROC PROD PROE "]
#write file_type filename [beg nb] [end ne ] [skip ns] [waitfor nw] [sel selection] [molecule_number]

 set num_steps [expr ($num_steps + 1)]

        # Prints the RMSD of the protein atoms between each timestep
        # and the first timestep for the given molecule id (default: top)

        set outDataFile [open CD-rmsd.dat w]

                set reference [atomselect top  "segid PROA and resid 1 to 166 and name CA" frame 0]
                set compare [atomselect top  "segid PROA and resid 1 to 166 and name CA"]

                for {set frame 0} {$frame < $num_steps} {incr frame} {
                        $compare frame $frame
                        set trans_mat [measure fit $compare $reference]
                        $compare move $trans_mat
                        set rmsd [measure rmsd $compare $reference]
                        # print the RMSD
                        puts "RMSD of $frame is $rmsd "
                        puts $outDataFile "$frame $rmsd"
                }

 close $outDataFile

 set num_steps [expr ($num_steps - 1)]
 set sel [atomselect top "segid PROA and resid 1 to 166 and name CA"]

 set outfile [open CD-rmsf.dat w]
for {set i 0} {$i < [$sel num]} {incr i} {
set alpharmsf [measure rmsf $sel first 1 last $num_steps step 1]
  puts $outfile "[expr {$i+1}] [lindex $alpharmsf $i]"
}
 close $outfile
########################################################3
 set num_steps [expr ($num_steps + 1)]

        # Prints the RMSD of the protein atoms between each timestep
        # and the first timestep for the given molecule id (default: top)

        set outDataFile [open HVR-rmsd.dat w]

                set reference [atomselect top  "segid PROA and resid 167 to 184 and name CA" frame 0]
                set compare [atomselect top  "segid PROA and resid 167 to 184 and name CA"]

                for {set frame 0} {$frame < $num_steps} {incr frame} {
                        $compare frame $frame
                        set trans_mat [measure fit $compare $reference]
                        $compare move $trans_mat
                        set rmsd [measure rmsd $compare $reference]
                        # print the RMSD
                        puts "RMSD of $frame is $rmsd "
                        puts $outDataFile "$frame $rmsd"
                }

 close $outDataFile

 set num_steps [expr ($num_steps - 1)]

 set sel [atomselect top "segid PROA and resid 167 to 184 and name CA"]

 set outfile [open HVR-rmsf.dat w]
#set alpharmsf [measure rmsf $sel first 1 last $num_steps step 1]
for {set i 0} {$i < [$sel num]} {incr i} {
set alpharmsf [measure rmsf $sel first 1 last $num_steps step 1]
  puts $outfile "[expr {$i+1}] [lindex $alpharmsf $i]"
}
 close $outfile

exit
