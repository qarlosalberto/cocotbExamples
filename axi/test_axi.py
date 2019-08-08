# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from cocotb.drivers.amba import AXI4LiteMaster
from cocotb.drivers.amba import AXIProtocolError

@cocotb.coroutine
def gen_clk(clk, period):
    while True:
        clk.value = 0
        yield Timer(period/2)
        clk.value = 1
        yield Timer(period/2)

@cocotb.test()
def axi_test(dut):
    CLK_PERIOD = 10
    axim = AXI4LiteMaster(dut, "s_axi", dut.axi_aclk)
    #clk
    clk = dut.axi_aclk
    cocotb.fork(gen_clk(clk, CLK_PERIOD))
    #reset
    dut.axi_aresetn = 1
    yield Timer(CLK_PERIOD * 10)
    #write
    ADDRESS = 0x00
    DATA = 0xAB
    yield axim.write(ADDRESS, DATA)
    value = yield axim.read(ADDRESS+0x04)

    print("Value = " + str(value))

    yield Timer(500)
