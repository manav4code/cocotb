HDL_TOPLEVEL_LANG ?= verilog
PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)
VERILOG_SOURCES = $(PWD)/../design/adder.sv
COMPILE_ARGS += -Padder.DATA_WIDTH=5
TOPLEVEL := adder
MODULE := test_adder
include $(shell cocotb-config --makefiles)/Makefile.sim
