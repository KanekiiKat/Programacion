from src.duplicate_encoder import duplicate_encode
import pytest

@pytest.mark.duplicate_encoder
def test_duplicate_encoder():
    assert duplicate_encode("din"),"((("
    assert duplicate_encode("recede"),"()()()"
    assert duplicate_encode("Success"),")())())"
    assert duplicate_encode("(( @"),"))(("