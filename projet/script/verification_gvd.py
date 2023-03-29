from os import path
import csv
import glob
from setup_logs import file_info
import pandas as pd


class verification_gvd:
    def __init__(self):
        self.log = file_info()

    def get_import_csv(self):
        try:
            self.csv_import = glob.glob(
                path.join(
                    path.dirname(path.abspath(__file__)),
                    "..",
                    "data",
                    "input/import.csv",
                )
            )
            self.log.info("Fichier import détécté.")

        except:
            self.log.warning("Fichier import non détecté.")

    def get_export_csv(self):
        try:
            self.csv_export = glob.glob(
                path.join(
                    path.dirname(path.abspath(__file__)),
                    "..",
                    "data",
                    "input/export.csv",
                )
            )

            self.log.info("Fichier export détécté.")
        except:
            self.log.warning("Fichier export non détecté.")

    def read_csv_files(self):
        try:
            self.df_first = pd.read_csv(
                self.csv_import[-1],
                on_bad_lines="skip",
                sep=";",
                skiprows=1,
                encoding="utf-8",
            )
            self.log.info("Lecture du fichier csv_import.")
        except:
            self.log.warning("Lecture du fichier csv_import impossible.")

        try:
            self.df_second = pd.read_csv(
                self.csv_export[-1],
                on_bad_lines="skip",
                sep=";",
                skiprows=1,
                encoding="utf-8",
            )
            self.log.info("Lecture du fichier csv_export.")
        except:
            self.log.warning("Lecture du fichier csv_export impossible.")

    def get_differences(self, outpt_name):
        try:
            result_diff = self.df_first[
                ~self.df_first.apply(tuple, 1).isin(self.df_second.apply(tuple, 1))
            ]
            result_diff.to_excel(outpt_name, index=False)
            self.log.info("Analyse effectuée.")
        except:
            self.log.warning("Analyse impossible.")


if __name__ == "__main__":
    verification_gvd = verification_gvd()
    verification_gvd.get_import_csv()
    verification_gvd.get_export_csv()
    verification_gvd.read_csv_files()
    verification_gvd.get_differences(outpt_name="result.xlsx")
