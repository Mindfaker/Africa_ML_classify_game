import os
import pandas as pd


class Train_Data():
    one_hot_unique_col = ['sex', 'marital_status', 'birth_year', 'branch_code', 'occupation_code','occupation_category_code']
    def __init__(self, train_data_path):
        self.raw_data_path = train_data_path
        self.raw_df = self.raw_clear_data()


    def read_data(self, data_path: str):
        """

        读取原始数据

        :param data_path:
        :return:
        """
        if os.path.exists(data_path):
            return pd.DataFrame()
        try:
            data = pd.read_csv(data_path)
            # 将婚姻情况的标识符 统一成大小写
            data["marital_status"] = data["marital_status"].apply(lambda x: str(x).upper())
            return data
        except:
            raise Exception("file is Not Csv Format")


    def one_hot_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """

        对需要进行处理的数据进行one-hot编码

        :param raw_data:
        :return:
        """
        if raw_data == None or raw_data.empty:
            return pd.DataFrame()
        for one_hot_col in Train_Data.one_hot_unique_col:
            one_hot_unique_values = list(raw_data[one_hot_col].unique())
            for one_hot_unique_value in one_hot_unique_values:
                raw_data[one_hot_col + "_" + one_hot_unique_value] = raw_data[one_hot_col].apply(lambda x : int(x == one_hot_unique_value))
        return raw_data


    def raw_clear_data(self):
        raw_data = self.read_data(self.raw_data_path)
        data = self.one_hot_data(raw_data=raw_data)
        return data

if __name__ == '__main__':
    pass