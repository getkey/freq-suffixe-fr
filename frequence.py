#!/usr/bin/env python3

import pandas as pd

def suffix_freq(df: pd.DataFrame, suffix: str):
	fem_sing = df[(df["genre"] == "f") & (df["nombre"] == "s")]
	masc_sing = df[(df["genre"] == "m") & (df["nombre"] == "s")]
	in_fem = fem_sing[fem_sing["phon"].str.endswith(suffix)]
	res = pd.merge(in_fem, masc_sing, on=["lemme", "cgram"])
	res["freq"] = (res["freqlemfilms2_x"] + res["freqlemlivres_x"]) / 2
	res = res.sort_values(by="freq", ascending=False)
	return res[["freq", "lemme", "cgram"]]


def main():
	pd.set_option("display.max_rows", None)

	df = pd.read_csv("./Lexique383/Lexique383.tsv", sep="\t")
	in_df = suffix_freq(df, "in")
	en_df = suffix_freq(df, "En")
	print(f"in: {in_df['freq'].sum()}\nain/ien/ein: {en_df['freq'].sum()}")

if __name__ == "__main__":
	main()
