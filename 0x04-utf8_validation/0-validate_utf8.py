#!/usr/bin/python3
"""
Validate if a given data set represents valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes.

    Returns:
        bool: True if valid UTF-8 encoding, False otherwise.
    """
    n_bytes = 0

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count leading ones to determine how many bytes in this UTF-8 char
            mask = 0x80
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # If no leading ones, it's a 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 encoding can only be from 1 to 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
            # Already counted byte, so expect n_bytes-1 continuation bytes
            n_bytes -= 1
        else:
            # Check if byte starts with '10'
            if not (byte & 0x80 and not (byte & 0x40)):
                return False
            n_bytes -= 1

    # All continuation bytes should be used up
    return n_bytes == 0
