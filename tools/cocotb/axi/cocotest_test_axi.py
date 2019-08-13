from cocotb_test.run import run
import pytest
import os

#SIM=ghdl pytest -s cocotest_test_axi.py
@pytest.mark.skipif(os.getenv("SIM") == "icarus", reason="VHDL not suported")
def test_adder_vhdl():
    run(vhdl_sources=["../../../hdl/axi.vhd","../../../hdl/axi_pkg.vhd"],
        simulation_args=["--vcd=func.vcd"],
        toplevel="axi",
        module="test_axi",
        toplevel_lang="vhdl"
    )
