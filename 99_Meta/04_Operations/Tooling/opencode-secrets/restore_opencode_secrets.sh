#!/usr/bin/env bash
set -euo pipefail

DEFAULT_BUNDLE="$HOME/Obsidian-vaults/Study-vault/99_Meta/04_Operations/Tooling/opencode-secrets/opencode-secrets-latest.tar.gpg"
BUNDLE="${1:-$DEFAULT_BUNDLE}"

ALLOWED=(
  ".local/share/opencode/auth.json"
  ".config/opencode/opencode.jsonc"
  ".zshrc"
)

fail() {
  printf '%s\n' "error: $1" >&2
  exit 1
}

contains_allowed() {
  local item="$1"
  local allowed
  for allowed in "${ALLOWED[@]}"; do
    if [[ "$item" == "$allowed" ]]; then
      return 0
    fi
  done
  return 1
}

collect_passphrase() {
  if [[ -n "${OPENCODE_SYNC_PASSPHRASE:-}" ]]; then
    PASSPHRASE="$OPENCODE_SYNC_PASSPHRASE"
    return
  fi

  if [[ -t 0 ]]; then
    read -r -s -p "Enter sync passphrase: " PASSPHRASE
    printf '\n'
    return
  fi

  fail "set OPENCODE_SYNC_PASSPHRASE or run interactively"
}

[[ -f "$BUNDLE" ]] || fail "bundle not found: $BUNDLE"
collect_passphrase

mapfile -t MEMBERS < <(
  gpg --batch --yes --pinentry-mode loopback --passphrase "$PASSPHRASE" --decrypt "$BUNDLE" \
    | tar -tzf -
)

[[ ${#MEMBERS[@]} -gt 0 ]] || fail "bundle has no files"

for member in "${MEMBERS[@]}"; do
  [[ "$member" != /* ]] || fail "refusing absolute path from archive: $member"
  [[ "$member" != *".."* ]] || fail "refusing parent path reference from archive: $member"
  contains_allowed "$member" || fail "unexpected file in archive: $member"
done

gpg --batch --yes --pinentry-mode loopback --passphrase "$PASSPHRASE" --decrypt "$BUNDLE" \
  | tar -xzf - -C "$HOME"

chmod 600 "$HOME/.local/share/opencode/auth.json" 2>/dev/null || true
chmod 600 "$HOME/.config/opencode/opencode.jsonc" 2>/dev/null || true
chmod 600 "$HOME/.zshrc" 2>/dev/null || true

printf '%s\n' "Restored files from: $BUNDLE"
printf '%s\n' "Reload shell env with: source ~/.zshrc"
printf '%s\n' "Verify MCP with: opencode mcp list"
