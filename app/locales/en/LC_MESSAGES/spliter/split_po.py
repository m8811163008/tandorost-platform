import os

def split_po_files_by_exercise(input_filename='messages_current.po', limit=29):
    """
    Splits a .po file into multiple files, where each output file 
    contains a maximum number of exercises (defined by 'limit').
    """
    try:
        if not os.path.exists(input_filename):
            print(f"Error: Input file '{input_filename}' not found.")
            return

        # Use a local buffer list within the function
        buffer = []
        exercise_count = 0
        file_counter = 1

        with open(input_filename, mode='r', encoding='utf-8') as infile:
            for line in infile:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Check for the start of a new exercise block
                if 'TITLE' in line and 'msgid' in line:
                    exercise_count += 1
                    
                    # If we have reached the limit, save the current buffer to disk
                    if exercise_count > 1 and (exercise_count - 1) % limit == 0:
                        output_filename = f"part_{file_counter}.po"
                        with open(output_filename, mode='w', encoding='utf-8') as outfile:
                            outfile.writelines(buffer)
                        print(f"Saved {output_filename} (contains up to exercise {exercise_count-1})")
                        
                        # Clear buffer for the next chunk
                        buffer.clear()
                        file_counter += 1

                # Add the current line to the buffer
                buffer.append(line)
            
            # Save any remaining lines after the loop finishes
            if buffer:
                output_filename = f"part_{file_counter}_final.po"
                with open(output_filename, mode='w', encoding='utf-8') as outfile:
                    outfile.writelines(buffer)
                print(f"Saved remaining part to '{output_filename}'")

    except IOError as e:
        print(f"An I/O error occurred: {e}")

# This runs the function when the script is executed:
if __name__ == "__main__":
    # You can change the limit here if needed, e.g., limit=10
    split_po_files_by_exercise(limit=29) 
