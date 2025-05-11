import requests
import os
import time
from datetime import datetime

class BitcoinBlockAlert:
    def __init__(self):
        self.last_block_height = None
        self.api_url = "https://blockchain.info/latestblock"

    def get_latest_block(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"获取区块信息时出错: {e}")
            return None

    def format_time(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%Y年%m月%d日 %H:%M:%S')

    def speak_block_info(self, block_data):
        block_height = block_data['height']
        block_time = self.format_time(block_data['time'])
        message = f"发现新区块！区块高度：{block_height}，区块时间：{block_time}"
        print(message)
        os.system(f'say "{message}"')

    def run(self):
        print("比特币爆块提醒器已启动...")
        while True:
            block_data = self.get_latest_block()
            if block_data and (self.last_block_height is None or block_data['height'] > self.last_block_height):
                self.speak_block_info(block_data)
                self.last_block_height = block_data['height']
            time.sleep(10)

if __name__ == "__main__":
    alert = BitcoinBlockAlert()
    alert.run() 