from argparse import ArgumentParser
import globals


def load_args():
    parser = ArgumentParser()

    parser.add_argument("-usr", "--user-data-dir", dest="userDataDir", help="Open specified user data dir")
    parser.add_argument("-c", "--config", dest="configFile", help="Open specified config file")
    parser.add_argument("-l", "--log-dir", dest="logDir", help="Open specified log dir")
    parser.add_argument("-a", "--exchange-file", dest="authFile", help="Open specified exchange.yml file")

    args = parser.parse_args()

    if args.userDataDir:
        globals.user_data_dir = args.userDataDir

    if args.logDir:
        globals.log_dir = args.logDir

    if args.configFile:
        globals.config_file_path = args.configFile

    if args.authFile:
        globals.auth_file_path = args.authFile
