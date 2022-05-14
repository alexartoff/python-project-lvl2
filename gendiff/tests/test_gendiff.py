import pytest
from gendiff import generate_diff
# from gendiff.parser import files_parser


@pytest.fixture
def file_one_j():
    # return 'gendiff/tests/fixtures/file1.json'
    return 'file1.json'


@pytest.fixture
def file_two_j():
    # return'gendiff/tests/fixtures/file2.json'
    return'file2.json'


@pytest.fixture
def file_one_y():
    # return 'gendiff/tests/fixtures/file1.yml'
    return 'file1.yml'


@pytest.fixture
def file_two_y():
    # return'gendiff/tests/fixtures/file2.yaml'
    return'file2.yaml'


@pytest.fixture
def file_three_y():
    # return 'gendiff/tests/fixtures/file3.yaml'
    return 'file3.yaml'


@pytest.fixture
def file_four_y():
    # return 'gendiff/tests/fixtures/file4.yaml'
    return 'file4.yaml'


@pytest.fixture
def file_one_tree_j():
    # return 'gendiff/tests/fixtures/file1tree.json'
    return 'file1tree.json'


@pytest.fixture
def file_two_tree_j():
    # return 'gendiff/tests/fixtures/file2tree.json'
    return 'file2tree.json'


@pytest.fixture
def file_one_tree_y():
    # return 'gendiff/tests/fixtures/file1tree.yml'
    return 'file1tree.yml'


@pytest.fixture
def file_two_tree_y():
    # return 'gendiff/tests/fixtures/file2tree.yaml'
    return 'file2tree.yaml'


@pytest.fixture
def result12():
    return open('gendiff/tests/fixtures/result12.txt', 'r')


@pytest.fixture
def result21():
    return open('gendiff/tests/fixtures/result21.txt', 'r')


@pytest.fixture
def result34():
    return open('gendiff/tests/fixtures/result34.txt', 'r')


@pytest.fixture
def result43():
    return open('gendiff/tests/fixtures/result43.txt', 'r')


@pytest.fixture
def result12tree():
    return open('gendiff/tests/fixtures/result12tree.txt', 'r')


@pytest.fixture
def result12treeplain():
    return open('gendiff/tests/fixtures/result12treeplain.txt', 'r')


@pytest.fixture
def result12treejson():
    return open('gendiff/tests/fixtures/result12treejson.txt', 'r')


def test_gendiff(
        file_one_j, file_two_j,
        file_one_y, file_two_y,
        file_three_y, file_four_y,
        result12, result21,
        result34, result43):
    res12 = result12.read()
    res21 = result21.read()
    res34 = result34.read()
    res43 = result43.read()
    assert generate_diff(file_one_j, file_two_j) == res12
    assert generate_diff(file_two_j, file_one_j) == res21
    assert generate_diff(file_one_y, file_two_y) == res12
    assert generate_diff(file_two_y, file_one_y) == res21
    assert generate_diff(file_one_j, file_two_y) == res12
    assert generate_diff(file_two_j, file_one_y) == res21
    assert generate_diff(file_one_y, file_two_j) == res12
    assert generate_diff(file_two_y, file_one_j) == res21
    assert generate_diff(file_three_y, file_four_y) == res34
    assert generate_diff(file_four_y, file_three_y) == res43


def test_gendiff_tree(
        file_one_tree_j, file_two_tree_j,
        file_one_tree_y, file_two_tree_y,
        result12tree, result12treeplain, result12treejson):
    res12 = result12tree.read()
    res12plain = result12treeplain.read()
    res12json = result12treejson.read()
    assert generate_diff(file_one_tree_j,
                         file_two_tree_j) == res12
    assert generate_diff(file_one_tree_y,
                         file_two_tree_y) == res12
    assert generate_diff(file_one_tree_j,
                         file_two_tree_j,
                         format='plain') == res12plain
    assert generate_diff(file_one_tree_y,
                         file_two_tree_y,
                         format='plain') == res12plain
    assert generate_diff(file_one_tree_j,
                         file_two_tree_j,
                         format='json') == res12json
    assert generate_diff(file_one_tree_y,
                         file_two_tree_y,
                         format='json') == res12json
