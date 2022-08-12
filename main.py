#!/usr/bin/env python3

from pathlib import Path
from dataclasses import dataclass

def main():
	words = set(parse(Path('./fr.dic').read_text()))
	simple_in_ending = {
		w for w in words if (
			w.word.endswith("in")
			and 'F.' in w.flags
			and not any(w.word.endswith(suffix) for suffix in ["ain", "ein"])
		)
	}
	complex_in_ending = {
		w for w in words if (
			w.word.endswith("ain") or w.word.endswith("ein")
			and 'F.' in w.flags
		)
	}
	print(sorted(map(lambda w : w.word, simple_in_ending)))
	print(sorted(map(lambda w : w.word, complex_in_ending)))
	print(len(simple_in_ending), len(complex_in_ending))

@dataclass(order=True, frozen=True)
class Word:
	word: str
	flags: str = ""

def parse(dic_file: str):
	return [ Word(*line.split('/')) for line in dic_file.splitlines()[2:] ]

if __name__ == '__main__':
	main()
