import os

def load_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def save_file(content, file_path, output_dir='.'):
    output_file_path = os.path.join(output_dir, "output", file_path)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as outp_f:
        outp_f.write(content)
        print(f"Written to {output_file_path}")