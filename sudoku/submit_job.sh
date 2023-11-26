#!/usr/bin/env bash
#
# You should only work under the /scratch/users/<username> directory.
#
# Example job submission script
#
# -= Resources =-
#
#SBATCH --job-name=sudoku-jobs
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --partition=shorter
#SBATCH --time=01:00:00
#SBATCH --output=part-a-sudoku.out
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
module load gcc/11.2.0

echo

echo "Running Job...!"
echo "==============================================================================="
echo "Running compiled binary..."

make
# #PART B:
# for ITER in 1 2 3
# do
#     for THREAD_COUNT in 32
#     do
#         for PROBLEM in 1 2 3 
#         do
#             EXEC="sudoku_solver_b"
#             FILENAME="perf-test-b/perf-${EXEC}-4x4_hard_${PROBLEM}-${THREAD_COUNT}-${ITER}.txt"
#             export OMP_NUM_THREADS=${THREAD_COUNT}
#             echo "Performing: ${FILENAME}"
#             "./${EXEC}" 16 "grids/4x4_hard_${PROBLEM}.csv" > ${FILENAME}
#         done
#     done
# done


# PART A:
for ITER in 1 2 3
do
    export OMP_NUM_THREADS=32
    FILENAME="perf-test-a/perf-sudoku_solver_serial-${ITER}.txt"
    echo "Performing: ${FILENAME}"
    ./sudoku_solver_serial 16 grids/4x4_hard_3.csv > ${FILENAME}

    for THREAD_COUNT in 32
    do
        for EXEC in "sudoku_solver_a" "sudoku_solver_b" 
        do
            FILENAME="perf-test-a/perf-${EXEC}-${THREAD_COUNT}-${ITER}.txt"
            echo "Performing: ${FILENAME}"
            export OMP_NUM_THREADS=${THREAD_COUNT}
            "./${EXEC}" 16 grids/4x4_hard_3.csv > ${FILENAME}
        done

        FILENAME="perf-test-a/perf-sudoku_solver_c-${THREAD_COUNT}-${ITER}.txt"
        echo "Performing: ${FILENAME}"
        export OMP_NUM_THREADS=${THREAD_COUNT}
        ./sudoku_solver_c 16 grids/4x4_hard_3.csv > ${FILENAME}
    done

    export OMP_NUM_THREADS=32
    FILENAME="perf-test-a/perf-sudoku_solver_c_serial-${ITER}.txt"
    echo "Performing: ${FILENAME}"
    ./sudoku_solver_c_serial 16 grids/4x4_hard_3.csv > ${FILENAME}
done


# EXECUTABLE="./${1:-"sudoku_solver_serial"}"
# THREAD_COUNT=${2:-32}
# PERF_FILENAME="perf-${EXECUTABLE}-${THREAD_COUNT}-${3}.txt"

# echo "Parallel version with ${THREAD_COUNT} threads"
# export OMP_NUM_THREADS=${THREAD_COUNT}
# # make
# ${EXECUTABLE} 16 grids/4x4_easy.csv > ${PERF_FILENAME}
 