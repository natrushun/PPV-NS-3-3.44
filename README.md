# PPV-NS-3-3.44

build:
cd ns-allinone-3.44/ns-3.44
./ns3 configure --enable-examples --enable-tests --with-python-bindings
./ns3 build


Python binding-hoz szükséges a cppyy, amihez egy virtuális környezetet létre kell hozni:
https://www.nsnam.org/docs/manual/html/python.html

