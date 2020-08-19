from collections import Counter
import re


class WordCounter:
    def __init__(self):
        self.word_count_hash_map = {}

    def parse_words(self, input_file: str) -> list:
        file_contents = self._open_text_file_as_str(input_file)
        if file_contents != "":
            return self._count_words(file_contents)
        return []

    def cumulative_word_count(self):
        return [
            item[0]
            for item in sorted(
                self.word_count_hash_map.items(), key=lambda x: (-x[1], x[0])
            )
        ]

    def _open_text_file_as_str(self, input_file: str) -> str:
        try:
            with open(input_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            return str()

    def _count_words(self, file_contents: str) -> dict:
        words = re.split(r"[\s,\.\n]", file_contents)
        words = list(filter(None, words))
        current_word_count_hash_map = {}
        for word in words:
            self._add_to_hash_map(word, current_word_count_hash_map)
        self.word_count_hash_map = dict(
            Counter(self.word_count_hash_map) + Counter(current_word_count_hash_map)
        )
        return [
            item[0]
            for item in sorted(
                current_word_count_hash_map.items(), key=lambda x: (-x[1], x[0])
            )
        ]

    def _add_to_hash_map(self, key: str, hash_map: dict):
        try:
            hash_map[key] += 1
        except KeyError:
            hash_map[key] = 1
