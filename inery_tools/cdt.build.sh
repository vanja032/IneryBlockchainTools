export Boost_INCLUDE_DIR="/root/inery/2.1/src/boost_1_72_0/"

rm -rf build/*
mkdir build
cd build
cmake ..
make -j 8

sudo make install