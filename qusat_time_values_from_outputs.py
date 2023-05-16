k = 250
l = 150

for i in range(50, k + 1, 200):
    with open(f"qusat_times_{i}.txt", "w") as output_file:
        for j in range(10, l + 1, 10):
            try:
                with open(f"qusat_output_{i}_{j}.txt", "r") as input_file:
                    lines = input_file.readlines()
                    last_line = lines[-1].strip()
                    last_int = int(''.join(filter(str.isdigit, last_line)))
                    file_name = f"qusat_output_{i}_{j}.txt"
                    output_file.write(str(last_int) + "\n")
            except FileNotFoundError:
                print(f"Could not find file qusat_output_{i}_{j}.txt")
