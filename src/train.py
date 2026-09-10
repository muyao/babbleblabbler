import gzip
import json
import sys
from pathlib import Path


def tokenise(data: str) -> list[str]:
	data_iter = iter(data)
	this_token = ""
	output_list: list[str] = []

	# Iterate through each char
	while True:
		this_char = next(data_iter, None)
		# Stop if end of string reached
		if this_char is None:
			break

		# If current char is space, break token
		if this_char.isspace():
			output_list.append(this_token)
			this_token = ""
			continue
		# If current char is not an alphabet, break token
		if not this_char.isalpha():
			output_list.append(this_token)
			this_token = ""
			output_list.append(this_char)
			continue
		# Otherwise, add to current token
		this_token += this_char

	# Remove whitespace and empty strings from output
	output_list = [
		token for token in output_list if not token.isspace() and token != ""
	]

	return output_list


def learn(tokens: list[str], ctxln: int) -> dict:
	output = {}

	for token_idx in range(len(tokens) - ctxln):
		# Using space as separator because it is definitely not a token
		k = " ".join(tokens[token_idx : token_idx + ctxln])

		# Add key to output dict if it doesn't exist
		if k not in output:
			output[k] = {}

		v = output[k]
		next_token = tokens[token_idx + ctxln]

		if next_token not in v:
			v[next_token] = 0

		v[next_token] += 1

	return output


def main() -> None:

	if len(sys.argv) != 3:
		raise Exception(
			f"Usage: {sys.executable} {sys.argv[0]} <training_file> <output_dir>"
		)

	# Training file path
	training_path = Path(sys.argv[1])
	# If path doesn't exist, error
	if not training_path.exists():
		raise Exception()
	# Error if path is not a file
	if not training_path.is_file():
		raise Exception()

	# Output json path
	output_path = Path(sys.argv[2])

	# Read training data from file
	with open(training_path, "r") as f:
		training_data = f.read()

	tokens = tokenise(training_data)

	# Clear output file before appending
	with open(output_path, "w") as f:
		f.write("")

	for i in range(3):
		with gzip.open(output_path, "ab") as f:
			f.write(json.dumps(learn(tokens, i + 1)).encode("utf-8"))
			f.write(b"\n")


if __name__ == "__main__":
	main()
