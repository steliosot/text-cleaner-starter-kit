def test_clean_file():
    import cleaner.clean  # runs the cleaner script
    text = open("data/clean/output.txt", "r", encoding="utf-8").read().strip()
    assert "hello world" in text
