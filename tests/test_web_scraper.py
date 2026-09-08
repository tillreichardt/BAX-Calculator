from unittest.mock import patch

import pytest

from src.scraper.web_scraper import get_bax, vorsaison


def test_vorsaison_regular():
    assert vorsaison("2025/26") == "2024/25"
    assert vorsaison("2026/27") == "2025/26"


def test_vorsaison_across_decade_boundary():
    assert vorsaison("2020/21") == "2019/20"


@patch("src.scraper.web_scraper.get_bax_alle")
def test_get_bax_returns_exact_season(mock_get_bax_alle):
    mock_get_bax_alle.return_value = {
        "einzel": [("2025/26", 475), ("2024/25", 435), ("2023/24", 410)],
        "doppel": [],
        "mixed": [],
    }

    assert get_bax("Till", "Reichardt", "BC Düsseldorf", "einzel", "2025/26") == 475
    assert get_bax("Till", "Reichardt", "BC Düsseldorf", "einzel", "2024/25") == 435


@patch("src.scraper.web_scraper.get_bax_alle")
def test_get_bax_falls_back_to_most_recent_earlier_season(mock_get_bax_alle):
    # Spieler hat 2024/25 nicht gespielt (kein Eintrag) -> nächstälterer Eintrag greift
    mock_get_bax_alle.return_value = {
        "einzel": [("2025/26", 487), ("2023/24", 481), ("2022/23", 453)],
        "doppel": [],
        "mixed": [],
    }

    assert get_bax("Daniel", "Springob", "BSC Hilden", "einzel", "2024/25") == 481


@patch("src.scraper.web_scraper.get_bax_alle")
def test_get_bax_raises_when_no_earlier_season_exists(mock_get_bax_alle):
    mock_get_bax_alle.return_value = {
        "einzel": [("2025/26", 500)],
        "doppel": [],
        "mixed": [],
    }

    with pytest.raises(ValueError):
        get_bax("Neuling", "Spieler", "Irgendein Verein", "einzel", "2024/25")
