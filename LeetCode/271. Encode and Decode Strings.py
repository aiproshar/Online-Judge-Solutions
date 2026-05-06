class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.

        Format: each string is encoded as <length>#<string>
        e.g. ["hello", "world"] -> "5#hello5#world"
        This handles any string content safely because we always
        know exactly how many characters to read after the #.
        """
        # We must work with list, as string is immutable, everytime we append it creates a new string
        # Appending N items in string -> N ^2
        stream = []
        for item in strs:
            n = str(len(item))
            # Prefix each string with its length followed by a # delimiter
            for char in n:
                stream.append(char)
            stream.append("#")
            # Then append the string itself
            for char in item:
                stream.append(char)
        return "".join(stream) # Converting the list to string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        if s == "" or s is None:
            return []
        strs = []
        i = 0
        while i < len(s):
            # I made a mistake not including ord(O)
            # I initially add ord(1) - ord(9) , this introduced infinite loop on len containing zeros (10, 20,100)
            if ord("0") <= ord(s[i]) <= ord("9"):
                # Read all consecutive digits to get the length prefix
                # (supports multi-digit lengths like "12" for longer strings)

                str_len = s[i]
                i += 1
                while ord("0") <= ord(s[i]) <= ord("9"):
                    str_len = str_len + s[i]
                    i += 1
                # Skip past the # delimiter
                i = i + 1
                # Extract exactly str_len characters — this is what makes the
                # encoding safe: even if the string contains digits or #, we
                # just read the exact known length and move on
                str_len = int(str_len)
                strs.append(s[i: i + str_len])
                i = i + str_len
        return strs
# Time Complexity: O(n)
# Space complexity: O(n)
# For a string of K , log(10)K + 1 space is required, which is negligible, observable universe has 10^80 atoms
# If your interviewer is paranoid, you can give explain atoms in observable universe
