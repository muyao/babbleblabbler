# Babbleblabbler

Not a real LLM, just generates text that looks real

---

## Installation

* **Run this:**
   ```bash
   git clone https://github.com/muyao/babbleblabbler.git 
   cd babbleblabbler
   ```

* **The Demo:**
   ```bash
   python src/generate.py demo/model.gz 400
   ```

---

## Training

1. Make a text file containing the contents to train on.

2. Run `train.py`:
   ```bash
   python src/train.py <training_path> <output_path> 10
   ```

3. To generate, run `generate.py`:
   ```bash
   python src/generate.py <model_path> 400
   ```

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

---

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

---

Fri, 11 Sep 2026 15:53:29 GMT