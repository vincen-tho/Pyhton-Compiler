# Tugas Besar IF2124 - Teori Bahasa Formal dan Otomata
## Compiler Bahasa Python
**Kelompok** : Trio Formal
* 13520064 - Ziyad Dhia Rafi
* 13520068 - Muhammad Naufal Satriandana
* 13520093 - Vincent Ho

### Files :
Berikut ini adalah list file beserta penjelasannya:
* `cfg.txt` -> File yang berisi Context Free Grammar(CFG) yang belum diubah menjadi CNF
* `cnf.txt` -> File yang berisi productions yang sudah dalam bentuk Chomsky Normal Form (di convert dari cfg.txt menggunakan file CFG2CNF.py)
* `CFG2CNF.py` -> File yang berisi algoritma untuk meng-convert dari bentuk CFG ke CNF (diambil dari https://github.com/adelmassimo/CFG2CNF)
* `helper.py` -> File yang berisi fungsi dan prosedur yang membantu proses konversi dari CFG ke CNF (diambil dari https://github.com/adelmassimo/CFG2CNF)
* `input.txt` -> File yang akan dicompile
* `lexer.py` -> File yang berisi fungsi yang berperan mengubah input file menjadi token yang kemudian akan diolah menggunakan algoritma CYK.
* `cyk.py` -> File yang berisi fungsi dan prosedur yang berhubungan dengan implementasi algoritma CYK
* `main.py` -> File yang befungsi sebagai driver untuk menjalankan program kami

