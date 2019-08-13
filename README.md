# Dependencies

- cocotb
```
pip install cocotb
```

- Edalize
```
pip install edalize
```

- GHDL
```
apt install ghdl
```

- cocotb-test
```
pip install cocotb-test
```

# Tests tools

## cocotb-test

```
cd /tools/cocotb/axi; SIM=ghdl pytest -s cocotest_test_axi.py

```
```
cd /tools/cocotb/simple; SIM=ghdl pytest -s cocotest_test_adder.py
```

## cocotb

```
cd /tools/cocotb/axi; make

```
```
cd /tools/cocotb/simple; make
```

## Edalize

```
cd /tools/edalize; python edalize_simple_ghdl.py

```
