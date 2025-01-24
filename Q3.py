def combine_lists():
    # Prompt the user to enter two lists in a specific format.
    user_input = input("Enter two lists of equal length in the format: [a,b,c], [1,2,3]: ")
    
    try:
        # Split the input into two parts based on "],"
        lists_str = user_input.split("],")
        if len(lists_str) != 2:
            print("Invalid input format. Please use the format: [a,b,c], [1,2,3].")
            return
        
        # Clean up and remove brackets from both parts
        list1_str = lists_str[0].strip().replace("[", "").replace("]", "")
        list2_str = lists_str[1].strip().replace("[", "").replace("]", "")
        
        # Split each part by comma and strip whitespace
        list1 = [item.strip() for item in list1_str.split(",") if item.strip() != ""]
        list2 = [item.strip() for item in list2_str.split(",") if item.strip() != ""]
        
        # Check if both lists have the same length
        if len(list1) != len(list2):
            print("Error: The two lists must have the same length.")
            return
        
        # Alternate elements from list1 and list2
        combined = []
        for x, y in zip(list1, list2):
            combined.append(x)
            combined.append(y)
        
        # Print the combined result in bracket notation
        print(f"[{','.join(combined)}]")
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    combine_lists()
