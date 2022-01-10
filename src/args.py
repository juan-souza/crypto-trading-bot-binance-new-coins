from argparse import ArgumentParser
import pathlib
import globals


def load_args():
    parser = ArgumentParser()
    parser.add_argument("-usr", "--user-data-dir", dest="userDataDir", help="Open specified user data dir")
    parser.add_argument("-c", "--config", dest="configFile", help="Open specified config file")
    parser.add_argument("-l", "--log-dir", dest="logDir", help="Open specified log dir")
    parser.add_argument("-a", "--exchange-file", dest="authFile", help="Open specified exchange.yml file")
    args = parser.parse_args()

    if args.userDataDir:
        user_data_dir = args.userDataDir
    else:
        user_data_dir = f"{pathlib.Path(__file__).parent.parent}/user_data"

    if args.logDir:
        log_dir = args.logDir
    else:
        log_dir = f"{user_data_dir}/logs"

    if args.configFile:
        config_file_path = args.configFile
    else:
        config_file_path = f"{user_data_dir}/config.yml"

    if args.authFile:
        auth_file_path = args.authFile
    else:
        auth_file_path = f"{user_data_dir}/auth.yml"

    # set path global
    globals.user_data_dir = user_data_dir
    globals.log_dir = log_dir
    globals.config_file_path = config_file_path
    globals.auth_file_path = auth_file_path
