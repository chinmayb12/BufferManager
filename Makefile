all: main data

main: main.cpp bufferManager.cpp bufferManager.hpp
	g++ -std=c++17 -o main main.cpp bufferManager.cpp

data: genData.cpp
	g++ -std=c++17 -o data genData.cpp

clean:
	rm -f data data.bin main