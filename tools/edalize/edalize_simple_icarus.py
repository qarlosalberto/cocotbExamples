import os
import shutil
import edalize

if (os.path.isdir('./build') == True):
    shutil.rmtree('./build')

work_root = 'build'

files = [
  {'name' : os.path.relpath('../../hdl/dump.v', work_root),
   'file_type' : 'verilogSource-2005'},
  {'name' : os.path.relpath('../../hdl/basic_and.v', work_root),
   'file_type' : 'verilogSource-2005'},
  {'name' : os.path.relpath('../../hdl/basic_and_tb.v', work_root),
   'file_type' : 'verilogSource-2005'}
]

tool = 'icarus'
edam = {
  'files'        : files,
  'name'         : 'test_icarus',
  'toplevel'     : 'basic_and_tb'
}

backend = edalize.get_edatool(tool)(edam=edam,
                            work_root=work_root)
os.makedirs(work_root)
backend.configure("")
backend.build()
backend.run("")
