from typing import Any
from beet import Context, BlockTag

def beet_default(ctx: Context):
    # print(ctx.data.block_tags.keys())
    for _, json_file in ctx.data.list_files(".json"):
        if type(json_file) is not BlockTag:
            # File is not a tag
            continue
        
        content: dict[str, Any]= json_file.ensure_deserialized()
        new_content = {}
        if "required" in content.keys():
            new_content["required"] = content["required"]

        # Wrap values
        values = []
        for value in content["values"]:
            if type(value) is str:
                values.append({"id": value, "required": False})
            else:
                values.append(value)

        new_content["values"] = values
        json_file.set_content(new_content)

# for root, _, files in walk('.'):
#     for file_name in files:
#         if not file_name.endswith('.json'):
#             continue
#         file_path = path.join(root, file_name)
#         print(f"Applying to {file_path}")
#         with open(file_path, "r") as f:
#             lines = f.readlines()

#         with open(file_path, "w+") as f:
#             for line in lines:
#                 if re.match(r'^\s*"[\w:/]*",?$\n?', line):
#                     f.write('    {"id":'
#                             + line.strip().replace(',', '')
#                             + ',"required":false}'
#                             + (',' if ',' in line else '')
#                             + '\n'
#                             )
#                 else:
#                     f.write(line)