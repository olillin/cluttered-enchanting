import re
from os import walk, path

for root, _, files in walk('.'):
    for file_name in files:
        if not file_name.endswith('.json'):
            continue
        file_path = path.join(root, file_name)
        print(f"Applying to {file_path}")
        with open(file_path, "r") as f:
            lines = f.readlines()

        with open(file_path, "w+") as f:
            for line in lines:
                if re.match(r'^\s*"[\w:/]*",?$\n?', line):
                    f.write('    {"id":'
                            + line.strip().replace(',', '')
                            + ',"required":false}'
                            + (',' if ',' in line else '')
                            + '\n'
                            )
                else:
                    f.write(line)