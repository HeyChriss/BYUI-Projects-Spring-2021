

with open("hr_system.txt") as a:

    for line in a:

        clean_line = line.strip()

        
        parts = clean_line.split(" ")

        
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])
        total = salary / 24

        
        if title.lower() == "engineer":
            total += 1000

        
        print(f"{name} (ID: {id_number}), {title} - ${total:.2f}")