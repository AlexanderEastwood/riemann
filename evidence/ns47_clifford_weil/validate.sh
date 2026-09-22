#!/bin/sh
# Build an isolated manuscript with the NS-47 fragment; do not edit the live tex.
set -eu
ns47_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
ns47_build=$(mktemp -d "${TMPDIR:-/tmp}/riemann-ns47-build.XXXXXX")
python3 - "$ns47_root" "$ns47_build" <<'PY'
from pathlib import Path
import shutil
import sys

root = Path(sys.argv[1])
build = Path(sys.argv[2])
ev = root / "evidence/ns47_clifford_weil"
target = build / "manuscript"
target.mkdir()
source = (root / "manuscript/fixed_space_prime_action_v1.tex").read_text()
anchor = r"\begin{thebibliography}{99}"
end = r"\end{thebibliography}"
assert source.count(anchor) == 1 and source.count(end) == 1
source = source.replace(anchor, (ev / "representation.tex").read_text() + "\n" + anchor)
source = source.replace(end, (ev / "bibitems.tex").read_text() + "\n" + end)
(target / "fixed_space_prime_action_v1.tex").write_text(source)
shutil.copy2(root / "manuscript/build.sh", target / "build.sh")
print(f"Isolated NS-47 validation build: {build}")
PY
(cd "$ns47_build" && ./manuscript/build.sh)
printf 'NS47_BUILD_DIR=%s\n' "$ns47_build"
