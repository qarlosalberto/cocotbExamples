# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from adder_model import adder_model
import random
from cocotb_coverage.coverage import *

@cocotb.coroutine
def gen_clk(clk, period):
    while True:
        clk.value = 0
        yield Timer(period/2)
        clk.value = 1
        yield Timer(period/2)

#functional coverage - check if all FIFO states have been reached
#and check if read or write operation performed in every FIFO state
FIFO_Coverage = coverage_section (
  CoverPoint("top.c", vname="C", bins = [True, False]),
  CoverPoint("top.(A <250)", xf = lambda dut,A,B,C : A<250, bins = [True, False]),
  CoverPoint("top.(A >250)", xf = lambda dut,A,B,C : A>250, bins = [True, False]),
  CoverCross("top.rwXfull", items = ["top.c", "top.(A <250)"]),
)

@FIFO_Coverage
def check(dut,A,B,C):
    if int(dut.X) != adder_model(A, B):
        raise TestFailure(
            "Randomised test failed with: %s + %s = %s" %
            (int(dut.A), int(dut.B), int(dut.X)))
    else:  # these last two lines are not strictly necessary
        dut._log.info("Ok!")

@cocotb.test()
def adder_random_test(dut):
    log = cocotb.logging.getLogger("cocotb.test") #logger instance
    PERIOD = 10
    clk = dut.clk
    cocotb.fork(gen_clk(clk, PERIOD))

    """Test for adding 2 random numbers multiple times"""
    yield Timer(20*PERIOD)

    for i in range(10):
        A = random.randint(0, 500)
        B = random.randint(0, 500)
        C = random.randint(0, 1)
        dut.A = A
        dut.B = B

        yield Timer(20*PERIOD)
        check(dut,A,B,C)

    #print coverage report
    coverage_db.report_coverage(log.info, bins=True)
