from multiprocessing import Pool 
 
def process_file(file_path): 
    with open(file_path) as f: 
        return sum(1 for line in f) 
 
# Count lines across multiple files in parallel 
with Pool() as p: 
    results = p.map(process_file, ["file1.csv", "file2.csv"]) 
  