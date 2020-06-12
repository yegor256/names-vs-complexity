#!/usr/bin/env ruby
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

require 'slop'

opts = Slop.parse(ARGV, strict: true, help: true) do |o|
  o.integer '--width', default: 9
  o.integer '--height', default: 5
  o.string '--xlabel', default: 'CC'
  o.string '--ylabel', default: 'Vars'
  o.string '--summary', default: 'summary.csv'
end

points = []

# Load CSV from summary

ymax = points.map { |p| p[:y] }.max
xmax = points.map { |p| p[:x] }.max

puts '\begin{tikzpicture}'
puts "\\begin{axis}[width=#{opts[:width]}cm,height=#{opts[:height]}cm,"
puts "axis lines=middle, xlabel={$#{opts[:xlabel]}$}, ylabel={$#{opts[:ylabel]}$},"
puts "xmin=#{points.map { |p| p[:x] }.min}, xmax=#{xmax},"
puts "ymin=#{points.map { |p| p[:y] }.min}, ymax=#{ymax},"
puts "extra tick style={major grid style=black},grid=major]"
puts "\\addplot [mark=*, only marks, mark size=0.8pt] coordinates {"
points.each do |p|
  puts "(#{p[:x]},#{p[:y]})"
end
puts "};"
puts '\end{axis}\end{tikzpicture}'
