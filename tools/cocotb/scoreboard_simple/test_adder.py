# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from adder_model import adder_model
import random
from cocotb.monitors import Monitor
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.scoreboard import Scoreboard
from cocotb.binary import BinaryValue

# ==============================================================================
class InputMonitor(Monitor):
    """Observes a single-bit input or output of DUT."""
    def __init__(self, name, signala, signalb, clock, callback=None, event=None):
        self.name = name
        self.signala = signala
        self.signalb = signalb
        self.clock = clock
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)

        while True:
            # Capture signal at rising edge of clock
            yield clkedge
            vec = [self.signala.value,self.signalb.value]
            self._recv(vec)
# ==============================================================================
class OutMonitor(Monitor):
    """Observes a single-bit input or output of DUT."""
    def __init__(self, name, signal, clock, callback=None, event=None):
        self.name = name
        self.signal = signal
        self.clock = clock
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)

        while True:
            # Capture signal at rising edge of clock
            yield clkedge
            vec = self.signal.value
            self._recv(vec)
# ==============================================================================
@cocotb.coroutine
def gen_clk(clk, period):
    while True:
        clk.value = 0
        yield Timer(period/2)
        clk.value = 1
        yield Timer(period/2)

class TB(object):
    def __init__(self, dut):
        self.dut = dut
        # Reconstruct the input transactions from the pins
        # and send them to our 'model'
        input_mon = InputMonitor("input", dut.A, dut.B, dut.clk,callback=self.adder_modelD)
        # Output monitor
        self.output_mon = OutMonitor("output", dut.X, dut.clk)
        # Create a scoreboard on the outputs
        self.expected_output = []
        self.scoreboard = Scoreboard(dut)
        self.scoreboard.add_interface(self.output_mon, self.expected_output)

    def adder_modelD(self,transaction):
        result = adder_model(transaction[0],transaction[1])
        self.expected_output.append(BinaryValue(value=result,n_bits=int(self.dut.DATA_WIDTH),bigEndian=False))

@cocotb.test()
def run_test(dut):
    #Setup test
    PERIOD = 10
    clk = dut.clk
    cocotb.fork(gen_clk(clk, PERIOD))

    tb = TB(dut)

    for _ in range(100):
        dut.A = random.randint(0,10)
        dut.B = random.randint(0,10)

        yield Timer(1*PERIOD)

    # Print result of scoreboard.
    raise tb.scoreboard.result
