# pdfProcesser

pdf --remove non-letters including formulas, pictures and other symbols which can not be recognized by txt
latex --remove formulas, citations, latex keywords

[Usage]
For pdf,
1 pdf2txt -o file.txt file.pdf 
2 python pdf/main.py -f file.txt

For latex,
python latex/main.py -f file.txt
