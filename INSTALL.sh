#!/usr/bin/env bash
# Install CODE ANLEITUNG Cursor rules (no PDFs).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
MDC="$ROOT/_framework/clean-code-framework.mdc"
JSON="$ROOT/_framework/coding-standards.json"

if [[ ! -f "$MDC" ]]; then
  echo "Missing: $MDC" >&2
  exit 1
fi

install_into() {
  local target="$1"
  mkdir -p "$target/.cursor/rules"
  cp "$MDC" "$target/.cursor/rules/clean-code-framework.mdc"
  cp "$JSON" "$target/.cursor/coding-standards.json"
  echo "Installed into project:"
  echo "  $target/.cursor/rules/clean-code-framework.mdc"
  echo "  $target/.cursor/coding-standards.json"
  echo "Restart Cursor / start a new chat."
}

if [[ "${1:-}" == "--global" ]]; then
  RULES="${HOME}/.cursor/rules"
  mkdir -p "$RULES"
  cp "$MDC" "$RULES/clean-code-framework.mdc"
  echo "Installed globally: $RULES/clean-code-framework.mdc"
  echo "Restart Cursor / start a new chat."
  exit 0
fi

TARGET="${1:-.}"
TARGET="$(cd "$TARGET" && pwd)"
install_into "$TARGET"
