from cocotb_test.run import run
import pytest
import os

#SIM=ghdl pytest -s cocotest_test_adder.py
@pytest.mark.skipif(os.getenv("SIM") == "icarus", reason="VHDL not suported")
def test_adder_vhdl():
    DATA_WIDTH = 5
    for i in range(2,DATA_WIDTH):
        run(vhdl_sources=["../../../hdl/adder.vhd"],
            simulation_args=["--vcd=func.vcd","-gDATA_WIDTH="+str(DATA_WIDTH)],
            toplevel="adder",
            module="test_adder",
            toplevel_lang="vhdl"
        )
