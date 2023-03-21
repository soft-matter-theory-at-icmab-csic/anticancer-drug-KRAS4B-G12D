#---------------------------------------------------------------------------------------
#calculate the cos-dihedral of two vetors along the trajectory
#---------------------------------------------------------------------------------------

from vmd import atomsel, molecule
import sys

f1 = open('cosTheta-dev1.dat','w')
mol = molecule.load('psf', "../../../step5_input.psf")
#mol = molecule.load("parm7", "../../../step7.parm7")
molecule.read(mol, "netcdf", "../../step7_50.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_55.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_60.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_65.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_70.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_75.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_80.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_85.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_90.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_95.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_100.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_105.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_110.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_115.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_120.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_125.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_130.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_135.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_140.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_145.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_150.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_155.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_160.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_165.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_170.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_175.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_180.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_185.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_190.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_195.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_200.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_205.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_210.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_215.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_220.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_225.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_230.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_235.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_240.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_245.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_250.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_255.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_260.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_265.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_270.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_275.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_280.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_285.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_290.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_295.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_300.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_305.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_310.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_315.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_320.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_325.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_330.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_335.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_340.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_345.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_350.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_355.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_360.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_365.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_370.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_375.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_380.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_385.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_390.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_395.nc", skip=5, waitfor=-1)
molecule.read(mol, "netcdf", "../../step7_400.nc", skip=5, waitfor=-1)

#traj = range(51,61)
#for a in traj:
#    molecule.read(mol, "netcdf", "../../step7_%a.nc", skip=10, waitfor=-1)

dt = 1         # ns

# magnitude of a vector
def magvect(v):
  magnitude = (v[0]*v[0] + v[1]*v[1] + v[2]*v[2])**0.5
  return magnitude


# cos-angle between vectors
def cos(v1,v2):
  v1v2=v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
  cos=v1v2/(magvect(v1)*magvect(v2))
  return cos


G1 = atomsel('resname LYS and resid 5 and name CA')        # C atom of melatonin
num_G1 = len(G1)                 # len(G1) = 1  
G1.frame

G2 = atomsel('resname VAL and resid 9 and name CA')      
num_G2 = len(G2)              
G2.frame

v2 = [0, 0, 1]                        # creating three lists of u2

timestep=molecule.numframes(mol)
for i in range(0, timestep):

    G1.frame = i
    G1.update() 
    x1 = G1.x[0]
    y1 = G1.y[0]
    z1 = G1.z[0] 
   
    G2.frame = i
    G2.update()  
    x2 = G2.x[0]
    y2 = G2.y[0]
    z2 = G2.z[0]
    
    v1=[0, 0, 0]  
    v1[0]=x2-x1
    v1[1]=y2-y1
    v1[2]=z2-z1

#    angle between vectors of v1i and v2i:  
    cosi = cos(v1, v2)
 
    f1.write(str(i*dt) + '\t' + str(cosi) + '\n')

f1.close()
sys.exit()
