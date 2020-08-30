from assignments.assignment_2.word_counter import WordCounter


class TestWordCount:
    def test_inexistent_file(self):
        word_counter = WordCounter()
        file = "tmp_file"

        assert word_counter.parse_words(file) == []

    def test_empty_file(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        assert word_counter.parse_words(file.realpath()) == []

    def test_no_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write("  ,\n.,   \n")
        assert word_counter.parse_words(file.realpath()) == []

    def test_count_simple_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write("Simple words words")
        assert word_counter.parse_words(file.realpath()) == ["words", "Simple"]

    def test_count_comma_sep_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write("Simple,words,words")
        assert word_counter.parse_words(file.realpath()) == ["words", "Simple"]

    def test_count_comma_space_sep_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write(" Simple , words,words ")
        assert word_counter.parse_words(file.realpath()) == ["words", "Simple"]

    def test_count_comma_space_dot_sep_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write(" Simple , words,words . words Simple.")
        assert word_counter.parse_words(file.realpath()) == ["words", "Simple"]

    def test_count_comma_space_dot_nl_sep_words(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write(" Simple , words,words . words Simple.\nwords,. Simple,.words")
        assert word_counter.parse_words(file.realpath()) == ["words", "Simple"]

    def test_count_cumulative(self, tmpdir):
        word_counter = WordCounter()
        file = tmpdir.mkdir("tmp_dir").join("tmp_file")

        file.write("Simple words words")
        word_counter.parse_words(file.realpath())

        file = tmpdir.mkdir("tmp_dir2").join("tmp_file2")
        file.write("simple, so so simple simple simple")
        word_counter.parse_words(file.realpath())
        assert word_counter.cumulative_word_count() == [
            "simple",
            "so",
            "words",
            "Simple",
        ]
