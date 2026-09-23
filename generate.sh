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

# The entry point is written by hand once and regenerated here, so adding a
# schema does not mean remembering to export it.
{
  echo "// $BANNER"
  echo
  echo "// One entry point, so a consumer writes \`from '@me-inn/leaf'\` and never a path"
  echo "// into this repository's layout. The layout is ours to change; the names are"
  echo "// the contract."
  echo "export type { Organization, TaxIdentifier, ContactPoint } from './organization';"
  echo "export type { Person } from './person';"
  echo "export type { Membership, Status as MembershipStatus } from './membership';"
  echo "export type { Participation, Context as ParticipationContext, Status as ParticipationStatus } from './participation';"
} > generated/typescript/index.ts

# One banner in every generated file, in each language's comment syntax, so
# whoever opens one knows before reading a line that editing it is pointless.
for f in generated/dart/*.dart generated/rust/*.rs generated/typescript/*.ts; do
  [ -e "$f" ] || continue
  printf '// %s\n\n%s' "$BANNER" "$(cat "$f")" > "$f"
done
for f in generated/python/*.py; do
  [ -e "$f" ] || continue
  printf '# %s\n\n%s' "$BANNER" "$(cat "$f")" > "$f"
done

echo "done"
