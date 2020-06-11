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

all: install search clone calc summary draw article

install:
	bundle update
	gem install volatility

clean:
	rm -rf *.tex
	rm -rf repos.txt
	rm -rf summary.csv
	rm -rf clones
	cd paper; latexmk -c

# search:
# 	ruby find-repos.rb | tee repos.txt

# clone:
# 	while read line; do \
# 		p="clones/$${line}"; \
# 		if [ -e "$${p}/.git" ]; then \
# 			echo "$${p} already here"; \
# 		else \
# 			mkdir -p "$${p}"; \
# 			git clone --depth=1 "https://github.com/$${line}" "$${p}"; \
# 		fi \
# 	done < repos.txt

# uncalc:
# 	find metrics -name 'scv.m' -exec rm \{} \;
# 	find metrics -name 'scv*.m' -exec rm \{} \;

# metrics=files bytes scv32 scv64 scv128

# calc:
# 	for f in $$(find clones/ -type directory -depth 2); do \
# 	  f=$${f/clones\/\//}; \
# 	  mkdir -p "metrics/$${f}"; \
# 		p="metrics/$${f}/files.m"; \
# 		if [ ! -e "$${p}" ]; then \
# 			find "clones/$${f}" -type file -not -path '.git/*' | wc -l > "$${p}"; \
# 		fi; \
# 		p="metrics/$${f}/bytes.m"; \
# 		if [ ! -e "$${p}" ]; then \
# 			du -s -b "clones/$${f}" | awk '{ print $$1 }' > "$${p}"; \
# 		fi; \
# 		for z in 32 64 128; do \
# 			p="metrics/$${f}/scv$${z}.m"; \
# 			if [ ! -e "$${p}" ]; then \
# 				/code/volatility/bin/volatility --sectors=$${z} --home="clones/$${f}" > "$${p}"; \
# 			fi; \
# 		done; \
# 	done

# summary:
# 	for i in ${metrics}; do \
# 		s="summary-$${i}.csv"; \
# 		rm -rf $${s}; \
# 		touch $${s}; \
# 		for f in $$(find metrics -name $${i}.m); do \
# 			cat "$${f}" >> $${s}; \
# 		done; \
# 		echo "$$(wc -l < $${s}) repos measured $${i}, summary in $${s}"; \
# 	done

# draw: summary-files.csv summary-bytes.csv
# 	for z in 32 64 128; do \
# 		ruby draw.rb --yaxis=summary-scv$${z}.csv --xaxis=summary-files.csv '--xlabel=log_{10}(M_1)' > paper/files-$${z}.tex; \
# 		ruby draw.rb --yaxis=summary-scv$${z}.csv --xaxis=summary-bytes.csv '--xlabel=log_{10}(M_2)' > paper/bytes-$${z}.tex; \
# 	done

# metrics:
# 	rm -f paper/total.tex
# 	echo "\\\def\\\thetotalrepos{$$(find metrics -name 'files.m' | wc -l)}" > paper/total.tex

article: paper/article.tex
	cd paper; rm -f article.pdf; latexmk -pdf article
