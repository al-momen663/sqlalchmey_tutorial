with open("huge_dataset.csv", "r") as f: 
    chunk = [] 
    for i, line in enumerate(f): 
        if i % 100000 == 0 and i > 0:  # Process every 100k rows 
            process_chunk(chunk)  # Your analytics function 
            chunk = [] 
        chunk.append(line.strip().split(",")) 
