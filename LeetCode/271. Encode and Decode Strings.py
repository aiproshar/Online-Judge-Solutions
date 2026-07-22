class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        Format: each string becomes <length>.<string>
        e.g. ["hello", "world"] -> "5.hello5.world"
        Length-prefixing is what makes this safe for arbitrary content:
        the decoder never has to guess where a string ends, it reads
        exactly as many characters as the prefix promised.
        """
        # Build in a list, not by += on a string. Strings are immutable, so
        # each += allocates a new one -> O(n^2) for n appends. join is O(n).
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))  # length prefix, may be multi-digit
            encoded.append('.')             # delimiter separating prefix from payload
            encoded.append(word)
        encoded = "".join(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []
        i = 0
        while i < len(s):
            # Read consecutive digits to recover the length prefix.
            # Must accept '0' too, omitting it breaks lengths like 10, 20, 100.
            current_len = []
            while ord('0') <= ord(s[i]) <= ord('9'):
                current_len.append(s[i])
                i += 1
            current_len = "".join(current_len)
            current_len = int(current_len)
            # skipping the '.'
            i += 1
            # Take exactly current_len characters. This is why the encoding is
            # safe even when the payload itself contains digits or '.' we
            # never scan for a delimiter inside the string.
            strs.append(s[i:i+current_len])
            i = i + current_len
        return strs

# Time:  O(n) -- each character is written once and read once.
# Space: O(n) for the output. The length prefix costs log10(k)+1 characters
# per string of length k, which is negligible.