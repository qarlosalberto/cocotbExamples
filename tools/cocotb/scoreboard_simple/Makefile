TOPLEVEL_LANG=vhdl
VHDL_SOURCES = $(PWD)/../../../hdl/adder.vhd
TOPLEVEL=adder
MODULE=test_adder
SIM=ghdl
SIM_ARGS=--vcd=func.vcd
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim
