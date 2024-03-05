from Menu import menu
import Data_operation

if __name__ == "__main__":
    df = Data_operation.import_csvfile()
    Data_operation.creat_json_profile(df[0],'list1')
    menu.main_window(df)