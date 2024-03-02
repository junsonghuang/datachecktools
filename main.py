from Menu import menu
import Data_operation

if __name__ == "__main__":
    df = Data_operation.import_csvfile()
    menu.main_window(df)