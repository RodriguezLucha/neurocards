import os
import re

import pytest


def starts_with_number_dash(string):
    return bool(re.match(r"^\d+-", string))


@pytest.mark.skip
def test_data_parse():
    # input:
    # 1- o – the
    # Ele é o único que me faz feliz.
    # He is the one who makes me happy.
    # 2- de – of, from
    # Eu preciso ver a página do livro
    # I need to see the page of the book.
    file = os.environ["CONVERTED_PATH"]
    f = open(file, "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        if not starts_with_number_dash(line):
            next
        else:
            print(line)
