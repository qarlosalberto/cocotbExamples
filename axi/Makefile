TOPLEVEL_LANG=vhdl
VHDL_SOURCES = $(PWD)/axi_pkg.vhd
VHDL_SOURCES += $(PWD)/axi.vhd
TOPLEVEL=axi
MODULE=test_axi
# TESTCASE=axi_test
SIM=ghdl
SIM_ARGS=--vcd=func.vcd
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim
