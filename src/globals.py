import os
import threading
import pathlib
import args

buy_ready = threading.Event()
sell_ready = threading.Event()
stop_threads = False
old_coins = {}
latest_listing = ""

user_data_dir = ""
log_dir = ""
config_file_path = ""
auth_file_path = ""

# Load Files path
args.load_args()

# Files name
currencies_file_name = f"{user_data_dir}/currencies.json"
old_coins_file_name = f"{user_data_dir}/old_coins.json"
sold_file_name = f"{user_data_dir}/sold.json"
order_file_name = f"{user_data_dir}/order.json"
session_file_name = f"{user_data_dir}/session.json"
test_new_listing_file_name = f"{user_data_dir}/test_new_listing.json"
test_new_listing_used_file_name = f"{user_data_dir}/test_new_listing.json.used"


#TRADE_OPTIONS config values
quantity = 15
pairing = "USDT"
test_mode = True
sl = -3
tp = 2
enable_tsl = True
tsl = -4
ttp = 2
