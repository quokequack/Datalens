
from unittest.mock import Mock

from app.service import AnalysisService


class TestAnalysisService:
    def test_analyze_bytes(self):
        reader = Mock()
        analyzer = Mock()

        reader.read_bytes.return_value = "fake_dataframe"
        analyzer.analyze.return_value = {
            "total_registros": 5
        }

        service = AnalysisService(reader, analyzer)

        result = service.analyze_bytes(b"fake_csv")

        reader.read_bytes.assert_called_once_with(
            b"fake_csv"
        )

        analyzer.analyze.assert_called_once_with(
            "fake_dataframe"
        )

        assert result["total_registros"] == 5
