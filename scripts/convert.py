#!/usr/bin/env python3.6

import os
import sys
import re
import nbconvert


name = sys.argv[1]
sheband = "#!/usr/bin/env python3.6"
notebook = name + ".ipynb"
scriptname = name + ".py"

os.chdir(os.path.join("..", "notebooks"))

code_lines = nbconvert.export_python(name + ".ipynb")[0]

code_lines = code_lines.split("\n")
code_lines = [line for line in code_lines if not (line.startswith("#") or line.startswith("get_ipython()"))]
code_lines = re.sub(r'\n\s*\n', r'\n\n', "\n".join(code_lines))


with open(scriptname, "w") as script:
    script.write("#!/usr/bin/env python3.6\n")
    script.write("#encoding: utf-8\n")
    for line in code_lines:
        script.write(line)
