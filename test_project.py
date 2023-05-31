from project import count_words,count_sentences,most_common_words

def test_count_words():
    assert count_words("I am my own hero") == 5

def test_count_sentences():
    assert count_sentences("I am my own hero. I will not falter. I will thrive even if it costs me my life.") == 3

def test_most_common_words():
    assert most_common_words("Evil will not be tolerated but it must not be extinguished, for there shall be no balance without it.",3)==[('BE', 3), ('NOT', 2), ('IT', 2)]

