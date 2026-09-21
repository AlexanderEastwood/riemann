#!/bin/sh
# Build the manuscript. Source validation is not a build: run this.
set -e
cd "$(dirname "$0")"
latexmk -pdf -interaction=nonstopmode fixed_space_prime_action_v1.tex
echo "--- pages: $(pdfinfo fixed_space_prime_action_v1.pdf | awk '/^Pages/{print $2}')"
grep -ci 'undefined\|multiply.defined' fixed_space_prime_action_v1.log \
  | xargs -I{} echo "--- undefined/duplicate references: {}"
