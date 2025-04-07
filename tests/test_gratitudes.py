from lib.gratitudes import Gratitudes

#test initial instance with no gratitudes added
def test_empty_instance():
    empty_gratitudes = Gratitudes()
    result = empty_gratitudes.format()
    assert result == "Be grateful for: ", 'returns "Be grateful for: " when no gratitudes added'

def test_single_addition():
    gratitudes = Gratitudes()
    gratitudes.add("sunsets")
    result = gratitudes.format()
    assert result == "Be grateful for: sunsets", 'returns "Be grateful for: sunsets" when "sunsets" added'

def test_multiple_additions():
    gratitudes = Gratitudes()
    gratitudes.add("sunsets")
    gratitudes.add("family")
    gratitudes.add("cat videos")
    result = gratitudes.format()
    assert result == "Be grateful for: sunsets, family, cat videos"