# The MIT License (MIT)
#
# Copyright (c) 2020 Yegor Bugayenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

SHELL := /bin/bash
all: install search clone calc summary draw article

install:
	bundle update
	python3 -m pip install -r requirements.txt

clean:
	rm -rf *.tex
	rm -rf repos.txt
	rm -rf summary.csv
	rm -rf clones
	cd paper; latexmk -c

search:
	ruby find-repos.rb | tee repos.txt

clone:
	while read line; do \
		p="clones/$${line}"; \
		if [ -e "$${p}/.git" ]; then \
			echo "$${p} already here"; \
		else \
			mkdir -p "$${p}"; \
			git clone --depth=1 "https://github.com/$${line}" "$${p}"; \
		fi \
	done < repos.txt

uncalc:
	rm -rf metrics

calc:
	mkdir -p metrics
	for r in $$(find clones/ -type d -maxdepth 2 ); do \
	  d="metrics/$${r/clones\/\//}"; \
		if [ -e "$${d}" ]; then \
		  echo "Dir with metrics already here: $${d}"; \
		else \
		  mkdir -p "$${d}"; \
		  for f in $$(find $${r} -name '*.java'); do \
		  	m="metrics/$${f/clones\/\//}.m"; \
		  	mkdir -p $$(dirname "$${m}"); \
				if [ ! -e "$${m}" ]; then \
					python3 computation/calc.py "$${f}" > "$${m}"; \
				fi \
			done; \
		  echo "$$(find $${d} -type f | wc -l) Java classes analyzed into $${d}"; \
		fi; \
	done

summary:
	s="summary.csv"; \
	rm -rf $${s}; \
	touch $${s}; \
	for f in $$(find metrics -name '*.m'); do \
		cat "$${f}" >> $${s}; \
	done; \
	echo "$$(wc -l < $${s}) methods measured, the summary is in $${s}"; \

draw: summary.csv
	ruby draw.rb --summary=summary.csv > paper/graph.tex

paper/total.tex:
	rm -f paper/total.tex
	echo "\\\def\\\thetotalrepos{$$(find metrics -name 'files.m' | wc -l)}" > paper/total.tex

article: paper/article.tex paper/total.tex
	cd paper; rm -f article.pdf; latexmk -pdf article
