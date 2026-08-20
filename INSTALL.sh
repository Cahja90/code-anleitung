#!/usr/bin/env bash
#installiert cursor-rules (keine pdfs)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
FRAMEWORK="$ROOT/_framework"
RULES=(clean-code-framework.mdc schreibweise.mdc)
JSON="$FRAMEWORK/coding-standards.json"
EDITOR="$FRAMEWORK/editorconfig"

for name in "${RULES[@]}"; do
  if [[ ! -f "$FRAMEWORK/$name" ]]; then
    echo "Missing: $FRAMEWORK/$name" >&2
    exit 1
  fi
done

install_rules() {
  local rules_dir="$1"
  mkdir -p "$rules_dir"
  for name in "${RULES[@]}"; do
    cp "$FRAMEWORK/$name" "$rules_dir/$name"
    echo "  $rules_dir/$name"
  done
}

if [[ "${1:-}" == "--global" ]]; then
  RULES_DIR="${HOME}/.cursor/rules"
  echo "Installed globally:"
  install_rules "$RULES_DIR"
  echo "Restart Cursor / start a new chat."
  exit 0
fi

TARGET="${1:-.}"
TARGET="$(cd "$TARGET" && pwd)"
echo "Installed into project:"
install_rules "$TARGET/.cursor/rules"
if [[ -f "$JSON" ]]; then
  cp "$JSON" "$TARGET/.cursor/coding-standards.json"
  echo "  $TARGET/.cursor/coding-standards.json"
fi
if [[ ! -f "$TARGET/.editorconfig" ]]; then
  cp "$EDITOR" "$TARGET/.editorconfig"
  echo "  $TARGET/.editorconfig"
fi
echo "Restart Cursor / start a new chat."
echo "Commit .cursor/rules/ and .editorconfig so the team uses the same rules."
