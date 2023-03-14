export BOOST_ROOT="/root/inery/2.1/src/boost_1_72_0/"
echo "$BOOST_ROOT"

rm -rf build/*
mkdir build
cd build
echo "Build directory"
cmake ..
make -j 8

sudo make install
