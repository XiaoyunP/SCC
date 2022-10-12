#!/bin/bash -l

#$ -P kamenet

# #$ -pe omp 16

#$ -l h_rt=12:00:00

ACTIVE=/projectnb/kamenet/xiaoyun/FHIaims/histamine_recal/v1/Au18/in_1

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE

ulimit -s unlimited

module load gcc/5.5.0
module load intel/2019.5
module load openmpi/3.1.4_intel-2019
module load cuda/9.2

#nohup mpirun -np 16 /projectnb/kamenet/Programs/FHIaims/fhi-aims.171221/bin/aims.171221_1.scalapack.mpi.x < /dev/null | tee aims.dft.out
nohup /projectnb/kamenet/Programs/FHIaims/fhi-aims.171221/bin/aitranss.060914.x > aitranss.out

