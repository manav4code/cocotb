HDL_TOPLEVEL_LANG ?= verilog
PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

# Add .sv files
VERILOG_SOURCES = $(PWD)/../design/

TOPLEVEL :=
MODULE := 

include $(shell cocotb-config --makefiles)/Makefile.sim
