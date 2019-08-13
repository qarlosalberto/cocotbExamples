import os
import shutil
import edalize

if (os.path.isdir('./build') == True):
    shutil.rmtree('./build')

work_root = 'build'

files = [
  {'name' : os.path.relpath('../../hdl/adder.vhd', work_root),
   'file_type' : 'vhdlSource-2008'},
  {'name' : os.path.relpath('../../hdl/adder_tb.vhd', work_root),
   'file_type' : 'vhdlSource-2008'}
]

tool = 'ghdl'
tool_options = {'analyze_options' : ['-fexplicit','--no-vital-checks','-frelaxed-rules'],
                'run_options' : ['--disp-time']
               }
edam = {
  'files'        : files,
  'name'         : 'test_ghdl',
  'tool_options' : {tool : tool_options},
  'toplevel'     : 'adder_tb'
}

backend = edalize.get_edatool(tool)(edam=edam,
                            work_root=work_root)
os.makedirs(work_root)
backend.configure("")
backend.build()
backend.run("")
