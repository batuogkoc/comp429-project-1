all: serial_c c b a serial

serial_c: sudoku_solver_c_serial.c
	gcc -o sudoku_solver_c_serial sudoku_solver_c_serial.c -fopenmp -lm

c: sudoku_solver_c.c
	gcc -o sudoku_solver_c sudoku_solver_c.c -fopenmp -lm

b: sudoku_solver_b.c
	gcc -o sudoku_solver_b sudoku_solver_b.c -fopenmp -lm

a: sudoku_solver_a.c
	gcc -o sudoku_solver_a sudoku_solver_a.c -fopenmp -lm

serial: sudoku_solver_serial.c
	gcc -o sudoku_solver_serial sudoku_solver_serial.c -fopenmp -lm

clean:
	rm -f sudoku_solver
