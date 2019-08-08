TOPLEVEL_LANG=vhdl
VHDL_SOURCES = $(PWD)/adder.vhd
TOPLEVEL=adder
MODULE=test_adder
TESTCASE=adder_basic_test,adder_random_test
SIM=ghdl
SIM_ARGS=--vcd=func.vcd
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim
