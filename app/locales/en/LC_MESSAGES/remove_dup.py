import os

def deduplicate_po_file(input_filepath, output_filepath):
    """
    Reads a .po file, removes duplicate 'msgid' entries, and writes the
    unique entries to a new file. Keeps the first instance found.
    
    Args:
        input_filepath (str): Path to the original .po file.
        output_filepath (str): Path where the deduplicated file will be saved.
    """
    print(f"Starting deduplication for: {input_filepath}")
    
    # Set to store all unique msgid values found
    seen_msgids = set()
    # List to hold the lines of the current message block (msgid, msgstr, and comments)
    current_block = []
    # List to hold the lines of the final, deduplicated file
    clean_lines = []
    
    # Flag to check if we are currently inside a message block that is a duplicate
    is_duplicate = False
    
    # Total count of message blocks (msgid/msgstr pairs) processed
    processed_blocks = 0
    # Count of blocks removed due to duplication
    removed_duplicates = 0

    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            for line in infile:
                # Store the line to the current block before processing
                current_block.append(line)

                # Check for the start of a new msgid block
                if line.startswith('msgid '):
                    # Process the previous block if it was valid (not an empty string msgid)
                    if current_block:
                        processed_blocks += 1
                    
                    # Extract the msgid value (the string in quotes)
                    # Example: msgid "SOME_KEY" -> "SOME_KEY"
                    # Using strip() to remove surrounding quotes and spaces
                    msgid_key = line.strip().split(' ', 1)[1].strip('"')
                    
                    # Reset the duplicate flag for the new block
                    is_duplicate = False
                    
                    if msgid_key in seen_msgids:
                        # Found a duplicate! Set flag to discard this block.
                        is_duplicate = True
                        removed_duplicates += 1
                        # Discard the previous lines (comments, etc.) that were added
                        # for this block *before* the msgid line was found.
                        current_block = [] 
                    else:
                        # This is a unique msgid. Add it to the set and prepare to keep the block.
                        seen_msgids.add(msgid_key)

                # Check for the start of a new msgstr block
                elif line.startswith('msgstr '):
                    # When we hit msgstr, the full block (comments, msgid, msgstr) is complete.
                    if not is_duplicate:
                        # Append the collected, unique block lines to the clean list
                        clean_lines.extend(current_block)
                        
                    # Reset the current block list for the next message entry (or file end)
                    current_block = []
                    is_duplicate = False # Reset just in case, though msgid line handles the main logic

                # Lines that are not 'msgid' or 'msgstr' (like comments, headers, continuation lines)
                # are just collected into the current_block until 'msgstr' is found.
                elif line.strip() == '':
                     # Keep empty lines outside of message blocks, but also append to current_block
                     # This helps preserve formatting/separation between entries.
                     if not current_block:
                         clean_lines.append(line)

    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
        return

    # Write the clean lines to the output file
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        outfile.writelines(clean_lines)

    print("-" * 40)
    print("✨ Deduplication complete! ✨")
    print(f"Total message blocks processed: {processed_blocks}")
    print(f"Unique message blocks saved: {len(seen_msgids)}")
    print(f"Duplicate blocks removed: {removed_duplicates}")
    print(f"Clean file saved to: {output_filepath}")

# --- Configuration ---
# **IMPORTANT:** Replace 'your_original_file.po' with the actual path to your 15K line file.
INPUT_FILE = 'messages.po' 
# The output file will contain the clean, deduplicated content.
OUTPUT_FILE = 'messages_c.po' 

# Run the function
if os.path.exists(INPUT_FILE):
    deduplicate_po_file(INPUT_FILE, OUTPUT_FILE)
else:
    # Use the sample data provided for demonstration if the real file is missing
    # In a real scenario, you'd just run the top block with your actual file path.
    print(f"Could not find '{INPUT_FILE}'. Using the sample data for demonstration.")
    
    # Create a temporary file with the sample and a deliberate duplicate
    temp_sample_data = """
msgid "E_D_SKULL_CRUSHER_CABLE_PREP_ONE"
msgstr "Lie on a bench with feet on the floor."

msgid "E_D_SKULL_CRUSHER_CABLE_PREP_TWO"
msgstr "Hold the barr in an overhand grip arms bent and elbows lifted."

# This is a duplicate msgid
msgid "E_D_SKULL_CRUSHER_CABLE_PREP_ONE"
msgstr "THIS IS THE DUPLICATE MESSAGE THAT WILL BE REMOVED."

msgid "E_D_SKULL_CRUSHER_CABLE_EXEC_ONE"
msgstr "Exhale and extend your elbows to press your hands up until your arms are straight."
"""
    TEMP_INPUT_FILE = 'temp_sample_input.po'
    TEMP_OUTPUT_FILE = 'temp_sample_output.po'
    with open(TEMP_INPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(temp_sample_data)
        
    deduplicate_po_file(TEMP_INPUT_FILE, TEMP_OUTPUT_FILE)
    # Clean up temp files
    # os.remove(TEMP_INPUT_FILE)
    # os.remove(TEMP_OUTPUT_FILE) # You can comment this out to inspect the output