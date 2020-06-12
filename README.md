[![latex](https://github.com/yegor256/names-vs-complexity/workflows/latex/badge.svg)](https://github.com/yegor256/names-vs-complexity/actions?query=latex)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/yegor256/names-vs-complexity/blob/master/LICENSE.txt)

Hypothesis: Java methods that contain variables with
[compound names](https://www.yegor256.com/2015/01/12/compound-name-is-code-smell.html)
tend to have larger
[cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity).

Method:

  * We take many big and popular Java repositories from GitHub
  * For each Java method we calculate: CC and count of compounds vars
  * We draw a graph: _x_ is CC, _y_ is the count
  * We make a conclusion about a correlation between them two

The results of this research will be published.
