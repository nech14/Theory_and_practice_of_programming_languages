import pytest
from src.specialDict import SpecialDict
from src.iloc import IlocException


class TestSpecialDict:

    def test_iloc(self):
        d = SpecialDict()
        d["value1"] = 1
        d["value2"] = 2
        d["value3"] = 3
        d["1"] = 10
        d["2"] = 20
        d["3"] = 30
        d["1, 5"] = 100
        d["5, 5"] = 200
        d["10, 5"] = 300
        assert d.iloc[0] == 10
        assert d.iloc[2] == 300
        assert d.iloc[5] == 200
        assert d.iloc[8] == 3
        with pytest.raises(IlocException):
            d.iloc[10]

    def test_ploc(self):
        d = SpecialDict()
        d["value1"] = 1
        d["value2"] = 2
        d["value3"] = 3
        d["1"] = 10
        d["2"] = 20
        d["3"] = 30
        d["(1, 5)"] = 100
        d["(5, 5)"] = 200
        d["(10, 5)"] = 300
        d["(1, 5, 3)"] = 400
        d["(5, 5, 4)"] = 500
        d["(10, 5, 5)"] = 600
        assert d.ploc[">=1"] == "{1=10, 2=20, 3=30}"
        assert d.ploc["<3"] == "{1=10, 2=20}"
        assert d.ploc[">0, >0"] == "{(1, 5)=100, (5, 5)=200, (10, 5)=300}"
        assert d.ploc[">=10,     >0"] == "{(10, 5)=300}"
        assert d.ploc["<5, >=5, >=3"] == "{(1, 5, 3)=400}"
        assert d.ploc["<0"] == ""
        assert d.ploc["==1"] == "{1=10}"
        assert d.ploc["<=2"] == "{1=10, 2=20}"
        assert d.ploc["<>1"] == "{2=20, 3=30}"