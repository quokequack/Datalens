from app.reader import CSVReader

class TestReader:
    def setup_method(self):
        self.reader = CSVReader()

    def test_read_bytes(self):
        content = b"name, age\nAna,20\nBruno,30"

        df = self.reader.read_bytes(content)

        assert len(df) == 2
        assert list(df.column) == ["name", "age"]
        