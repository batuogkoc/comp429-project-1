mandelbrot-kuacc: mandelbrot.cpp mandelbrot.hpp main.cpp
	g++ -Wall -Werror -W -Wextra -DKUACC main.cpp mandelbrot.cpp -fopenmp -std=gnu++11 -o ./mandelbrot


mandelbrot-vis: mandelbrot.cpp mandelbrot.hpp main.cpp
	g++ -Wall -Werror -W -Wextra main.cpp mandelbrot.cpp -fopenmp -lsfml-system -lsfml-window -lsfml-graphics -o ./mandelbrot -std=gnu++11

vis: mandelbrot-vis
	./mandelbrot

run: mandelbrot-kuacc
	./mandelbrot

clean:
	rm -f -- ./tags ./mandelbrot ./*.ppm
