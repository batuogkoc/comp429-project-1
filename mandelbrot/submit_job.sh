#!/usr/bin/env bash
#
# You should only work under the /scratch/users/<username> directory.
#
# Example job submission script
#
# -= Resources =-
#
#SBATCH --job-name=mandelbrot-jobs
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --partition=shorter
#SBATCH --time=00:05:00
#SBATCH --output=part-b.out
#SBATCH --qos=shorter
#SBATCH --mem-per-cpu=1G
################################################################################
##################### !!! DO NOT EDIT ABOVE THIS LINE !!! ######################
################################################################################
# Set stack size to unlimited
echo "Setting stack size to unlimited..."
ulimit -s unlimited
ulimit -l unlimited
ulimit -a

echo "Loading GCC 11..."
# module load gcc/11.2.0

echo

echo "Running Job...!"
echo "==============================================================================="
echo "Running compiled binary..."

echo "Parallel version with 16 threads"

export OMP_NUM_THREADS=32
# #PART A:
# for ITER in 1 2 3
# do
#     for CHUNK in 1 10 1000
#     do
#         FILENAME="perf-test-a/perf-mandelbrot-32-d-${CHUNK}-${ITER}.txt"
#         echo "Performing: ${FILENAME}"
#         make SCHEDULE="schedule(dynamic, ${CHUNK})"
#         ./mandelbrot > ${FILENAME}
#     done

    
#     FILENAME="perf-test-a/perf-mandelbrot-serial-${ITER}.txt"
#     echo "Performing: ${FILENAME}"
#     ./mandelbrot_serial > ${FILENAME}
# done

#Part b
for ITER in 1 2 3
do
    for THREAD_COUNT in 1 2 4 8 16 32
    do
        FILENAME="perf-test-b/perf-mandelbrot-${THREAD_COUNT}-d-${ITER}.txt"
        echo "Performing: ${FILENAME}"
        make SCHEDULE="schedule(dynamic)"
        ./mandelbrot > ${FILENAME}
    done
done