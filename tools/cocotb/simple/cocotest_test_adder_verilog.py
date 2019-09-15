from cocotb_test.run import run
import pytest
import os

#SIM=icarus pytest -s cocotest_test_adder.py
# @pytest.mark.skipif(os.getenv("SIM") == "icarus", reason="VHDL not suported")
def test_adder_vhdl():
    DATA_WIDTH = 5
    for i in range(2,DATA_WIDTH):
        run(verilog_sources=["../../../hdl/adder.v"],
            toplevel="adder",
            module="test_adder",
            toplevel_lang="verilog"
        )
