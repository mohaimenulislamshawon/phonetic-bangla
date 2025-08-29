# Phonetic-Bangla: Bengali Transliteration for Python

[![PyPI Version](https://badge.fury.io/py/phonetic-bangla.svg)](https://pypi.org/project/phonetic-bangla/)
[![Python Versions](https://img.shields.io/pypi/pyversions/phonetic-bangla.svg)](https://pypi.org/project/phonetic-bangla/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/mohaimenulislamshawon/phonetic-bangla/actions/workflows/ci.yml/badge.svg)](https://github.com/mohaimenulislamshawon/phonetic-bangla/actions)

**Tired of switching keyboards? Need to generate Bengali text programmatically in your Python project? This is the tool for you.**

`phonetic-bangla` is an intelligent, rule-based phonetic transliterator that converts English (Roman) script to Bengali (Bangla). It's designed for developers, data scientists, and anyone who finds it cumbersome to use a traditional Bengali keyboard but needs accurate Bengali text. Just type Bengali words as they sound in English, and this library will handle the rest.

## 🌟 Why Use Phonetic-Bangla?

*   ⌨️ **No Bengali Keyboard Needed**: Write Bengali using your standard English keyboard. Perfect for lazy typists and developers in a hurry.
*   🧠 **Intelligent & Context-Aware**: It's not just a simple character map. It understands context to correctly handle complex Bengali phonetics, like *Juktoborno* (conjuncts) and ambiguous sounds.
*   🐍 **Simple Python Integration**: A clean, memorable `bn()` function makes it incredibly easy to use in any Python script.
*   💻 **Powerful Command-Line Tool**: Need a quick conversion? Use it directly from your terminal.
*   🍃 **Zero Dependencies**: Pure Python, making it lightweight and easy to add to any project.

## 🚀 Quick Start

### 1. Installation

Install the package from PyPI with one simple command:

```bash
pip install phonetic-bangla
```
### 2. Usage in Python

Import the easy-to-use `bn` function and start converting. It's that simple.

```python
from phoneticbn import bn

# --- Basic Conversation ---
english_text = "amar sOnar bangla, ami tomay bhalobasi."
bengali_text = bn(english_text)

print(bengali_text)
# Output: আমার সোনার বাংলা, আমি তোমায় ভালোবাসি।

# --- Handling Complex Words ---
# The library's real power is in handling tricky cases automatically.
print(bn("sawgotom"))   # -> স্বাগতম
print(bn("dhonyobad"))   # -> ধন্যবাদ
print(bn("kormo"))      # -> কর্ম
```
### 3. Usage from the Command Line

You can also use the tool directly from your terminal for quick conversions.

```bash
phonetic-bangla "sobar jonyo shubhechha"
# Output: সবার জন্য শুভেচ্ছা
```
## 📖 The Complete Phonetic Guide

Master Bengali typing with this comprehensive cheat sheet. The engine is designed to be intuitive, but for perfect accuracy, use these specific rules for complex sounds.

### Vowels & Diacritics (Shoroborno & Kar)

| Bengali | English (Independent) | English (Diacritic) | Example (Phonetic -> Bengali) |
| :-----: | :-------------------: | :-----------------: | ----------------------------- |
|    অ    |           `o`           |     `(implicit)`    | `k` -> ক                      |
|    আ/া   |         `a`, `A`        |       `a`, `A`      | `baba` -> বাবা                |
|    ই/ি   |           `i`           |         `i`         | `din` -> দিন                  |
|    ঈ/ী   |         `I`, `ee`       |       `I`, `ee`     | `nodi`, `nodee` -> নদী         |
|    উ/ু   |           `u`           |         `u`         | `putul` -> পুতুল              |
|    ঊ/ূ   |         `U`, `oo`       |       `U`, `oo`     | `dUr`, `door` -> দূর           |
|    ঋ/ৃ   |          `rri`          |        `RI`         | `kRIpoN` -> কৃপণ              |
|    এ/ে   |           `e`           |         `e`         | `desh` -> দেশ                  |
|    ঐ/ৈ   |       `OI`, `E`       |     `OI`, `E`     | `bOI` -> বই              |
|    ও/ো   |           `O`           |         `O`         | `bhalo` -> ভালো               |
|    ঔ/ৌ   |          `OU`           |        `OU`         | `mOU` -> মৌ                   |

### Consonants (Banjonborno)

| Bengali | English | Example     | Bengali | English | Example    |
| :-----: | :-----: | ----------- | :-----: | :-----: | ---------- |
|    ক    |   `k`   | `kaka`      |    খ    |   `kh`  | `khobor`   |
|    গ    |   `g`   | `gan`       |    ঘ    |   `gh`  | `ghum`     |
|    ঙ    |   `Ng`  | `oNgko`     |    চ    |   `c`   | `cumu`    |
|    ছ    |   `ch`  | `chobi`     |    জ    |   `j`   | `jol`      |
|    ঝ    |   `jh`  | `jhoR`      |    ঞ    |   `NG`  | `miNGa`   |
|    ট    |   `T`   | `Taka`      |    ঠ    |   `Th`  | `Thik`     |
|    ড    |   `D`   | `Dal`       |    ঢ    |   `Dh`  | `Dhaka`    |
|    ণ    |   `N`   | `horiN`     |    ত    |   `t`   | `tumi`     |
|    থ    |   `th`  | `thala`     |    দ    |   `d`   | `dad`      |
|    ধ    |   `dh`  | `dhan`      |    ন    |   `n`   | `nodi`     |
|    প    |   `p`   | `pata`      |    ফ    |   `ph`  | `phul`     |
|    ব    |   `b`   | `baba`      |    ভ    |   `bh`  | `bhai`     |
|    ম    |   `m`   | `ma`        |    য    |   `z`/`y` | `zodi`/`byasto` |
|    র    |   `r`   | `rat`       |    ল    |   `l`   | `lal`      |
|    শ    |  `sh`/`S` | `shyamola`    |    ষ    |   `Sh`  | `bhaSha`   |
|    স    |   `s`   | `sokal`     |    হ    |   `h`   | `hat`      |
|    ড়    |   `R`   | `paR`       |    ঢ়    |   `Rh`  | `aShaRh`   |
|    য়    |   `y`   | `doya`      |    ৎ    |    `` ` ``   | `hoTa` + `` ` `` -> হঠাৎ |

### Juktoborno (Conjuncts) & Folas

This is where `phonetic-bangla` shines. Type consonants one after another, and the library will automatically create the conjunct.

| Desired Output   | Phonetic Input | Example Usage      | Notes                               |
| :--------------: | :------------: | :----------------- | ----------------------------------- |
| **হৃদয়** (Special) |   `hRidoy`     | `hRidoy` -> হৃদয়   | The only way to get **হৃ**.         |
|      **বিজ্ঞান**      |  `bijNGan`    | `bijNGan` -> বিজ্ঞান | For **জ্ঞ**, use `jNG`.              |
|      **লক্ষী**      |   `lokShI`   | `lokShmi` -> লক্ষী | For **ক্ষ**, use `kSh`.                |
|       **কর্ম**       |     `kormo`    | `kormo` -> কর্ম    | Use `rf` for explicit **রেফ (র্)**. |
|       **ব্যস্ত**       |    `byasto`    | `byasto` -> ব্যস্ত | `y` after a consonant is **য-ফলা**. |
|       **স্বাগতম**      |    `swagotom`  | `swagotom` -> স্বাগতম | `w` after a consonant is **ব-ফলা**. |
|       **শান্ত**       |    `shanto`    | `shanto` -> শান্ত  | `n` + `t` -> **ন্ত**.             |
|       **অঙ্ক**       |     `oNgko`    | `oNgko` -> অঙ্ক    | `Ng` + `k` -> **ঙ্ক**.              |

### Modifiers

| Name         | Bengali | Phonetic | Example Usage |
| :----------- | :-----: | :------: | :------------ |
| **Chandrabindu** |    ঁ    |  `C`, `nN` | `canNd`, `caCd`  -> চাঁদ  |
| **Anusvara**   |    ং    |    `ng`    | `rong` -> রং   |
| **Bisorgo**    |    ঃ    |  `:` or `H` | `du:kho`, `duHkho` -> দুঃখ |
| **Hosonto**    |    ্    |     `+`      | `shanto+` -> শান্ত্ |


## 🤝 Contributing
This project is built for the community, and contributions are highly welcome! If you find a word that doesn't transliterate correctly or have an idea for a new rule, please get involved.

1.  **Open an Issue**: The best way to start is by opening an issue on our [GitHub Issues](https://github.com/mohaimenulislamshawon/phonetic-bangla/issues) page. Describe the bug or feature request in detail.
    *   **For bugs**: Please provide the input you used and the incorrect output it generated.
2.  **Fork & Create a Pull Request**: If you'd like to fix the issue yourself, please fork the repository and submit a pull request with your changes. Be sure to add a test case that validates your fix.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mohaimenulislamshawon/phonetic-bangla/blob/main/LICENSE) file for full details.



