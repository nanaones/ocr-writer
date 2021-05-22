from typing import List
from unicodedata import normalize
import os


def run(pdf_language: str = "eng+kor"):
    _cli_pre = u"ocrmypdf -l " + pdf_language + " --output-type pdf "
    _file_format = u".pdf"
    print(_cli_pre)
    path = os.getcwd()
    pdf_list = _get_file_list(file_path=path, file_format=_file_format)
    cli_command_list = _complete_cli_command(pdf_file_list=pdf_list, _file_format=_file_format, _cli_pre=_cli_pre)
    [_run_shell(cli_command) for cli_command in cli_command_list]
    print("done")


def _complete_cli_command(_file_format: str = "", pdf_file_list: list = List[str], _cli_pre: str = ""):
    orc_pdf_list = [_.replace(_file_format, "-ocr" + _file_format) for _ in pdf_file_list]
    return [_cli_pre + pdf_file_list[origin_name_idx] + " " + orc_pdf_list[origin_name_idx] for origin_name_idx in range(len(pdf_file_list))]


def _get_file_list(file_path: str = "", file_format: str = ""):
    file_list = os.listdir(file_path)
    data_list = [normalize("NFC", file)for file in file_list if file.endswith(file_format) if "ocr" not in file ]
    print(data_list)
    return [data.replace("(", "\(").replace(")", "\)").replace(" ", "\ ") for data in data_list]


def _run_shell(cli_command: str = ""):
    with os.popen(cli_command) as stream:
        print(stream.readlines())
    pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:    
        run(sys.argv[1])
    else:
        run()
