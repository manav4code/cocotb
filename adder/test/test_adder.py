import os
import random
import sys
from pathlib import Path

import cocotb
from cocotb.triggers import Timer
from cocotb_tools.runner import get_runner

if cocotb.simulator.is_running():
    from adder_model import adder_model


@cocotb.test()
async def adder_random_test(dut):
    """Test: Adding 2 random numbers"""
    DATA_WIDTH = dut.DATA_WIDTH.value.to_unsigned()
    

    for i in range(10):
        in1 = random.randint(0, 2**DATA_WIDTH - 1)
        in2 = random.randint(0, 2**DATA_WIDTH - 1)
        cin = random.randint(0,  1)
        goldenOutput:int = adder_model(in1, in2, cin)

        dut.a_i.value = in1
        dut.b_i.value = in2
        dut.carry_i.value = cin

        

        await Timer(2, "ns")
        

        assert dut.sum_o.value == goldenOutput & (2**DATA_WIDTH - 1), f"[FAIL], Wrong Sum, Case: {dut.a_i.value} + {dut.b_i.value}"
        assert dut.carry_o.value == goldenOutput >> DATA_WIDTH, f"[FAIL], Wrong Carry out, Case: {dut.a_i.value} + {dut.b_i.value}"

def test_adder_runner():
    """Simulate the adder example using the Python runner"""

    # Makefile sets these variables
    # Setting 'verilog' and 'icarus' as default HDL and SIM
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    # Adding model dir to the path
    sys.path.append(str(proj_path/"model"))

    if hdl_toplevel_lang == "verilog":
        sources = [proj_path / "design" / "adder.sv"]
    else:
        print("Design should be written in Verilog HDL")
        exit()

    build_test_args = []

    # Adding tests to the path
    sys.path.append(str(proj_path / "test"))
    print(sys.path)

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="adder",
        always=True,
        build_args=build_test_args
    )
    runner.test(
        hdl_toplevel="adder", test_module="test_adder", test_args=build_test_args
    )


if __name__ == "__main__":
    test_adder_runner()



