from configparser import ConfigParser
from pathlib import Path


def get_file_path(filename='2.testdbconfig.ini'):
    this_path = Path(__file__).parent/filename
    if this_path.exists():
        return this_path
    else:
        raise FileNotFoundError('Do not found the ini file.')


def read_db_config(section='mysql'):
    """
    Read database configuration file and return a dictionary object
    :param filename: name of the configuration file.
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    try:
        filename = get_file_path()
    except FileNotFoundError as e:
        return e
    except Exception as e:
        return f'Unkown Error : {e}'
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section,
                                                               filename))
    # items 是以元组为元素的列表，每个元组包含两个元素，前为参数，后为参数值
    dicts = dict(items)
    # 由于端口读出来为字符串，因此需要在此处改为int
    if 'port' in dicts:
        dicts['port'] = int(dicts['port'])
    return dicts


if __name__ == "__main__":
    print(read_db_config())
