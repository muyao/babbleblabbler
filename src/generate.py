import gzip
import json
import random
import sys
from pathlib import Path

import config as c


def next_token(model: list[dict], prev_tokens: list[str]) -> str:

	next_token = random.choice(list(model[0].keys()))
	k = " ".join(prev_tokens)

	# Try through all n grams
	for i in range(c.MAX_N_GRAM):

		n_g = c.MAX_N_GRAM - i - 1

		all_nexts = model[n_g]

		if i < len(prev_tokens):
			k = " ".join(prev_tokens[i:])

		if k not in all_nexts:
			continue

		poss_nexts: dict[str, int] = all_nexts[k]

		next_token = random.choices(
			list(poss_nexts.keys()), weights=list(poss_nexts.values()), k=1
		)[0]

	return next_token


def main() -> None:
	if len(sys.argv) != 3:
		raise Exception(
			f"Usage: {sys.executable} {sys.argv[0]} <model_path> <num_tokens>"
		)

	# Model path
	model_path = Path(sys.argv[1])
	# If path doesn't exist, error
	if not model_path.exists():
		raise Exception()
	# Error if path is not a file
	if not model_path.is_file():
		raise Exception()

	num_tokens = int(sys.argv[2])

	with gzip.open(model_path, "rb") as f:
		model_bytes: list[bytes] = f.readlines()

	# Remove trailing newline
	model_bytes = [line.strip() for line in model_bytes]
	# Jsonify
	model: list[dict] = [json.loads(line) for line in model_bytes]

	token: str = random.choice(list(model[0].keys()))

	prev_tokens = []

	# Print tokens
	for i in range(num_tokens):
		# Previous tokens
		prev_tokens.append(token)
		if len(prev_tokens) > c.MAX_N_GRAM:
			del prev_tokens[0]

		# When to insert a space
		if token.isalpha() and i != 0:
			print(" ", end="")

		print(token, end="")

		token = next_token(model, prev_tokens)


if __name__ == "__main__":
	main()
