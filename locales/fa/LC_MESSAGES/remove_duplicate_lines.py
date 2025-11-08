import os
from typing import Set, List, Tuple

def remove_duplicate_po_entries(input_filepath: str, output_filepath: str):
    """
    Opens a .po file, removes duplicate 'msgid' entries and their subsequent 'msgstr' lines,
    and writes the unique entries to a new output file.

    Args:
        input_filepath: The path to the original .po file.
        output_filepath: The path to save the cleaned .po file.
    """
    # Use a set to store unique msgid strings encountered so far
    seen_msgids: Set[str] = set()
    # Use a list to store the final lines of the clean PO file
    unique_lines: List[str] = []
    
    # Flag to track if the current msgid line should be included
    is_unique: bool = False
    
    # Counters for logging
    duplicates_removed_count = 0

    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            for line in infile:
                # A .po file can have comments or context lines before the msgid
                stripped_line = line.strip()

                if stripped_line.startswith('msgid '):
                    # Extract the msgid value (the string content after 'msgid ')
                    # It might be wrapped in quotes
                    msgid_value = stripped_line[6:].strip().strip('"')
                    
                    if msgid_value not in seen_msgids:
                        # Found a unique msgid, so we'll keep this line and the next msgstr
                        seen_msgids.add(msgid_value)
                        unique_lines.append(line)
                        is_unique = True
                    else:
                        # This is a duplicate msgid
                        duplicates_removed_count += 1
                        is_unique = False
                        # We skip adding this line (the duplicate msgid)
                        
                elif stripped_line.startswith('msgstr '):
                    # Check the flag set by the *previous* msgid line
                    if is_unique:
                        # This msgstr belongs to a unique msgid, so keep it
                        unique_lines.append(line)
                    else:
                        # This msgstr belongs to a duplicate msgid, so skip it
                        pass
                        
                else:
                    # Keep all other lines (comments, context, empty lines, headers, etc.)
                    # unless we are actively skipping a block (i.e., msgid was a duplicate)
                    # We assume non-msgid/msgstr lines (like `msgctxt`) should be kept 
                    # and they usually appear before the 'msgid' line.
                    unique_lines.append(line)

        # Write the collected unique lines to the output file
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)
            
        print(f"✅ Successfully processed file: '{input_filepath}'")
        print(f"📝 Clean file saved to: '{output_filepath}'")
        print(f"🗑️ Total duplicate 'msgid' blocks removed: {duplicates_removed_count}")

    except FileNotFoundError:
        print(f"❌ Error: Input file not found at '{input_filepath}'")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Example Usage ---
# 1. Create a dummy input file based on your example
input_file_path = "messages.po"
output_file_path = "messages_o.po"

if __name__ == "__main__":
    remove_duplicate_po_entries(input_filepath=input_file_path, output_filepath = output_file_path) 