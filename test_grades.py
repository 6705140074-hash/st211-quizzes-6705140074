import pytest
from grades import letter_grade
def test_boundary_a_grade():
    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"

    def test_boundary_pass_fail():
        assert letter_grade(60) == "C"
        assert letter_grade(59) =="F"

        def test_minimun_vaild():
            assert letter_grade(0) == "F"

            def test_maximun_valid():
                assert letter_grade(100) == "A"

                def test_below_minimun_invalid():
                    with pytest.raises(ValueError):
                        letter_grade(-1)