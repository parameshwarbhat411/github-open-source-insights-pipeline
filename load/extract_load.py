import gzip
import shutil
import tempfile
import os
import duckdb
from datetime import datetime
import glob

class ExtractLoad:
    db_path = 'file.db'

    """
    function to unzip the gharchives folder and copy, paste the content
    to a temporary directory and Using the temporary directory as a source to
    ingest the data to duckDB table
    """
    def extract_load(self, source_directory,temp_dir_path):
        try:
            tmp_dir_name = tempfile.TemporaryDirectory(dir=temp_dir_path)
            print(tmp_dir_name.name)

            con = duckdb.connect(self.db_path)

            # Ensure the source schema exists
            con.execute("CREATE SCHEMA IF NOT EXISTS source")

            # Check if the table exists
            table_exists = con.execute(
                "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'src_gharchive' AND table_schema = 'source'"
            ).fetchone()[0]

            if not table_exists:
                # Create an empty table with the structure of the JSON files
                sample_json_file = None
                for filename in os.listdir(source_directory):
                    if filename.endswith('.json.gz'):
                        sample_json_file = os.path.join(source_directory, filename)
                        break

                if sample_json_file:
                    # Unzip the sample file temporarily to get the structure
                    dest_path = os.path.join(tmp_dir_name.name, 'sample.json')
                    with gzip.open(sample_json_file, 'rb') as f_in, open(dest_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)

                    # Create the table with the structure of the JSON file
                    con.execute(f"""
                        CREATE TABLE source.src_gharchive AS 
                        SELECT *, NOW() AS loaded_at FROM read_json_auto('{dest_path}') WHERE FALSE
                    """)

                files = glob.glob(f"{tmp_dir_name.name}/*.json")
                for f in files:
                    os.remove(f)

            # Get the maximum loaded_at value
            result = con.execute("SELECT MAX(loaded_at) FROM source.src_gharchive").fetchone()
            max_loaded_at = result[0].replace(tzinfo=None) if result[0] is not None else datetime.min


            for filename in os.listdir(source_directory):
                if filename.endswith('.json.gz'):
                    try:
                        # Extract the timestamp from the filename
                        file_timestamp_str = filename.split('.')[0]
                        file_timestamp = datetime.strptime(file_timestamp_str, '%Y-%m-%d')

                        # Only process files newer than the last load time
                        if file_timestamp > max_loaded_at:
                            file_path = os.path.join(source_directory, filename)
                            dest_path = os.path.join(tmp_dir_name.name, filename[:-3])

                            with gzip.open(file_path, 'rb') as f_in, open(dest_path, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                                print(f'Unzipped {filename} to {dest_path}')
                    except Exception as e:
                        print(f"Error processing file {filename}: {e}")

            json_files = glob.glob(f"{tmp_dir_name.name}/*.json")

            # Count the number of JSON files
            num_json_files = len(json_files)

            print(f"Number of JSON files: {num_json_files}")

            dir_name = f"{tmp_dir_name.name}/"
            if os.path.isdir(dir_name):
                if not os.listdir(dir_name):
                    print("Directory is empty, No files to load")
                else:
                    print("Directory is not empty")
                    # Insert new data into DuckDB with the current timestamp
                    json_files_directory = f"{tmp_dir_name.name}/*.json"
                    con.execute(f"""
                        INSERT INTO source.src_gharchive 
                        SELECT *, NOW() AS loaded_at FROM read_json_auto('{json_files_directory}')
                    """)
                    print(f"Loaded data into DuckDB at {self.db_path}")
            else:
                print("Given directory doesn't exist")

        except duckdb.DuckDBPyException as e:
            print(f"DuckDB error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            con.close()
            tmp_dir_name.cleanup()


if __name__ == '__main__':
    source_directory = '/Users/arjunbhat/github-stars-pipeline/data/gharchive_sample'
    temp_dir_path = '/Users/arjunbhat/github-stars-pipeline/data/'
    obj = ExtractLoad()
    obj.extract_load(source_directory,temp_dir_path)