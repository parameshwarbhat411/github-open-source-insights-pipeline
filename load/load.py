import os
import gzip
import shutil
import duckdb
import glob

newpath = r'/Users/arjunbhat/github-stars-pipeline/data/unzipped'
if not os.path.exists(newpath):
    os.makedirs(newpath)

source_directory = '/Users/arjunbhat/github-stars-pipeline/data/gharchive_sample'

for filename in os.listdir(source_directory):
    if filename.endswith('.json.gz'):
        file_path = os.path.join(source_directory, filename)
        dest_path = os.path.join(newpath, filename[:-3])

        with gzip.open(file_path, 'rb') as f_in, open(dest_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

json_files = glob.glob(f"{newpath}/*.json")

# Count the number of JSON files
num_json_files = len(json_files)

print(f"Number of JSON files: {num_json_files}")

files = glob.glob(f"{newpath}/*.json")
for f in files:
    os.remove(f)

# con = duckdb.connect('file.db')
#
# # Ensure the source schema exists
# con.execute("CREATE SCHEMA IF NOT EXISTS source")
#
# json_files_directory = f"{newpath}/*.json"
#
# con.execute(f"""
#         CREATE TABLE source.src_gharchive AS
#         SELECT *, NOW() AS loaded_at FROM read_json_auto('{json_files_directory}')
#         """)
#
# con.close()