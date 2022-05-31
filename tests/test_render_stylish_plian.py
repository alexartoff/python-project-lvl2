from gendiff import generate_diff


FORMATTER = 'stylish'
FILEMODE = 'plain'


def test_json(file1_json_path, file2_json_path, result_render):
    assert result_render == generate_diff(file1_json_path,
                                          file2_json_path,
                                          selected_format=FORMATTER)


def test_yml(file1_yml_path, file2_yml_path, result_render):
    assert result_render == generate_diff(file1_yml_path,
                                          file2_yml_path,
                                          selected_format=FORMATTER)
