'''
Docstring for strings.rabinkarpalgo
The Rabin-Karp algorithm is a string searching algorithm that uses hashing to find any one 
of a set of pattern strings in a text. It is particularly efficient for multiple pattern searches and 
works by comparing hash values of the pattern and substrings of the text.
'''
class RollingHash:
    def __init__(self, string: str) -> None:
        self._hash = 0
        self._chars = 0
        self._alphabet_size = 26

        for char in string:
            self.append(char)

    @staticmethod
    def _char_to_int(char: str) -> int:
        return ord(char) - ord("a") + 1

    def append(self, char: str) -> None:

        self._chars += 1
        self._hash = self._hash * self._alphabet_size + self._char_to_int(char)

    def popleft(self) -> None:
        self._chars -= 1
        self._hash %= self._alphabet_size ** self._chars

    def __eq__(self, other: object) -> bool:
        return isinstance(other, RollingHash) and self._hash == other._hash
    
    def first_match(string: str, pattern: str) -> int:
        string_hash = RollingHash(string[: len(pattern) - 1])
        pattern_hash = RollingHash(pattern)

        for end in range(len(pattern) - 1, len(string)):
            start = end - len(pattern) + 1

            string_hash.append(string[end])

            if string_hash == pattern_hash:
                # Check for collision
                if string[start : end + 1] == pattern:
                    return start

            string_hash.popleft()

        return -1

if __name__ == "__main__":
    text = "aba"
    pattern = "abc"
    result = RollingHash.first_match(text, pattern)
    print(f"Pattern found at index: {result}")  # Output: Pattern found at index: 2