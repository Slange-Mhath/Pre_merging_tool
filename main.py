import json
import logging
import numbers
from argparse import ArgumentParser

log = logging.getLogger(__name__)

# ElasticSearch expects these keys to have numeric values and will neglect the
# whole file if they don't.
# ["AppVersion", "ExifToolVersion", "ImageHeight", "ImageWidth", "Pages",
# "PDFVersion", "WordCount", "Words", "XResolution","YResolution"]


def open_json_file(f_path):
    with open(f_path, "r") as f:
        try:
            f = json.load(f)
        except ValueError:
            logging.error(f"{f_path} is not a valid json file")
        return f


def write_merged_f_log(modified_log, output_file):
    with open(output_file, "a", encoding="utf-8") as open_f:
        open_f.write(
            json.dumps(modified_log, sort_keys=True, ensure_ascii=True) + '\n')


def check_if_num(info, key):
    if isinstance(info[key], str):
        if info[key].isnumeric():
            # If value is str but numeric
            return True
    # If value of key is int, float or long
    if isinstance(info[key], numbers.Number):
        return True


def main(file_log_path, output_file):
    f = open_json_file(file_log_path)
    for info in f:
        if "AppVersion" in info.keys():
            if not check_if_num(info, "AppVersion"):
                del info["AppVersion"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "ExifToolVersion" in info.keys():
            if not check_if_num(info, "ExifToolVersion"):
                del info["ExifToolVersion"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "ImageHeight" in info.keys():
            if not check_if_num(info, "ImageHeight"):
                del info["ImageHeight"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "ImageWidth" in info.keys():
            if not check_if_num(info, "ImageWidth"):
                del info["ImageWidth"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "Pages" in info.keys():
            if not check_if_num(info, "Pages"):
                del info["Pages"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "PDFVersion" in info.keys():
            if not check_if_num(info, "PDFVersion"):
                del info["PDFVersion"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "Words" in info.keys():
            if not check_if_num(info, "Words"):
                del info["Words"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "XResolution" in info.keys():
            if not check_if_num(info, "XResolution"):
                del info["XResolution"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
        if "YResolution" in info.keys():
            if not check_if_num(info, "YResolution"):
                del info["YResolution"]
                logging.warning(
                    f"File: {info['SourceFile']} - Value of key 'YResolution' "
                    f"is not numeric "
                    f"and therefore deleted")
    write_merged_f_log(f, output_file)


if __name__ == "__main__":
    logging.basicConfig(filename="pre_merger.log",
                        filemode="a",
                        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s "
                               "%(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    parser = ArgumentParser(description="...")
    parser.add_argument("-file_log_path", metavar="file_log_path",
                        help="Path to the log file to make ready for merge")
    parser.add_argument("-output_file", metavar="output_file",
                        help="Path to file for the prepared log.")

    args = parser.parse_args()
    main(args.file_log_path, args.output_file)
