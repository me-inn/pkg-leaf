#!/usr/bin/env bash
# Generates the per-language types from the schemas. Nobody writes these by
# hand, and CI fails if anybody edits one — see .github/workflows/check.yml.
#
# The schema is the source of truth. The generated files are checked in so a
# consumer can read them without running anything, and regenerated here so
# they can never drift from the schema they came from.
set -euo pipefail
cd "$(dirname "$0")"

QUICKTYPE="npx --yes quicktype@23"
BANNER="Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh."

for schema in schemas/*.v1.json; do
  case "$schema" in schemas/common.v1.json) continue;; esac
  file="$(basename "$schema" .v1.json)"        # organization
  # The type name quicktype stamps on the root object.
  name="$(python3 -c "import sys;print(''.join(w.capitalize() for w in sys.argv[1].split('-')))" "$file")"

  echo "→ $name"
  $QUICKTYPE --src-lang schema --top-level "$name" --lang dart \
    -o "generated/dart/${file}.dart" "$schema"
  $QUICKTYPE --src-lang schema --top-level "$name" --lang rust \
    --visibility public --derive-debug --derive-clone -o "generated/rust/${file}.rs" "$schema"
  $QUICKTYPE --src-lang schema --top-level "$name" --lang typescript \
    --just-types --prefer-unions -o "generated/typescript/${file}.ts" "$schema"
  $QUICKTYPE --src-lang schema --top-level "$name" --lang python \
    --python-version 3.7 -o "generated/python/${file}.py" "$schema"
done

# The entry point, read back out of what was just generated rather than listed
# here. It used to be a hand-written list under a comment claiming that adding
# a schema did not mean remembering to export it — which was false, and cost
# three types that existed, compiled, and could not be imported by anybody.
#
# A name is exported bare while it is unique, and prefixed with its own type
# when two schemas both produce it: `Status` exists in more than one, and one
# of them would silently win.
python3 - "$BANNER" <<'PYTHON' > generated/typescript/index.ts
import re, sys, glob, os

banner = sys.argv[1]

# The shapes that live in common.v1 and are copied into every file that uses
# them. They are one type, so they are exported once under the name they have
# always had — a consumer importing ContactPoint must keep importing
# ContactPoint. Their home is person: the widest document that carries them.
SHARED = {'TaxIdentifier': 'TaxIdentifier', 'ContactPoint': 'ContactPoint',
          'LocalIds': 'LocalIds', 'Type': 'ContactPointType'}
SHARED_HOME = 'person'

exported = {}
for path in sorted(glob.glob('generated/typescript/*.ts')):
    stem = os.path.basename(path)[:-3]
    if stem == 'index':
        continue
    exported[stem] = re.findall(r'^export (?:interface|type|enum) (\w+)',
                                open(path).read(), re.M)

top = {stem: ''.join(w.capitalize() for w in stem.split('-')) for stem in exported}

print(f'// {banner}')
print()
print("// One entry point, so a consumer writes `from '@me-inn/leaf'` and never a path")
print("// into this repository's layout. The layout is ours to change; the names are")
print('// the contract.')
for stem in sorted(exported):
    parts = []
    for name in exported[stem]:
        if name == top[stem]:
            parts.append(name)
        elif name in SHARED:
            # Once, from its home. Everywhere else it is the same type again.
            if stem == SHARED_HOME:
                parts.append(name if SHARED[name] == name else f'{name} as {SHARED[name]}')
        else:
            # Always prefixed, never bare: two schemas each producing a Status
            # would otherwise have one of them silently win.
            parts.append(f'{name} as {top[stem]}{name}')
    if parts:
        print(f"export type {{ {', '.join(parts)} }} from './{stem}';")
PYTHON

# One banner in every generated file, in each language's comment syntax, so
# whoever opens one knows before reading a line that editing it is pointless.
for f in generated/dart/*.dart generated/rust/*.rs generated/typescript/*.ts; do
  [ -e "$f" ] || continue
  # index.ts already carries it: stamping again gave it the banner twice.
  case "$f" in generated/typescript/index.ts) continue;; esac
  printf '// %s\n\n%s' "$BANNER" "$(cat "$f")" > "$f"
done
for f in generated/python/*.py; do
  [ -e "$f" ] || continue
  printf '# %s\n\n%s' "$BANNER" "$(cat "$f")" > "$f"
done

echo "done"
