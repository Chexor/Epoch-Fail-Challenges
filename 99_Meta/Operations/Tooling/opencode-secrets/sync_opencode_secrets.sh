#!/usr/bin/env bash
set -euo pipefail

NEXTCLOUD_DIR="${NEXTCLOUD_DIR:-$HOME/Obsidian-vaults/Study-vault/99_Meta/04_Operations/Tooling/opencode-secrets}"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUTPUT="${1:-$NEXTCLOUD_DIR/opencode-secrets-${STAMP}.tar.gpg}"

FILES=(
  ".local/share/opencode/auth.json"
  ".config/opencode/opencode.jsonc"
  ".zshrc"
)

fail() {
  printf '%s\n' "error: $1" >&2
  exit 1
}

ensure_file_exists() {
  local path="$1"
  [[ -f "$HOME/$path" ]] || fail "missing required file: $HOME/$path"
}

collect_passphrase() {
  if [[ -n "${OPENCODE_SYNC_PASSPHRASE:-}" ]]; then
    PASSPHRASE="$OPENCODE_SYNC_PASSPHRASE"
    return
  fi

  if [[ -t 0 ]]; then
    read -r -s -p "Enter sync passphrase: " PASSPHRASE
    printf '\n'
    read -r -s -p "Confirm sync passphrase: " PASSPHRASE_CONFIRM
    printf '\n'
    [[ "$PASSPHRASE" == "$PASSPHRASE_CONFIRM" ]] || fail "passphrases did not match"
    unset PASSPHRASE_CONFIRM
    return
  fi

  fail "set OPENCODE_SYNC_PASSPHRASE or run interactively"
}

mkdir -p "$NEXTCLOUD_DIR"
chmod 700 "$NEXTCLOUD_DIR"

for f in "${FILES[@]}"; do
  ensure_file_exists "$f"
done

collect_passphrase

tar -czf - -C "$HOME" "${FILES[@]}" \
  | gpg --batch --yes --pinentry-mode loopback --passphrase "$PASSPHRASE" --symmetric --cipher-algo AES256 -o "$OUTPUT"

chmod 600 "$OUTPUT"
cp -f "$OUTPUT" "$NEXTCLOUD_DIR/opencode-secrets-latest.tar.gpg"
chmod 600 "$NEXTCLOUD_DIR/opencode-secrets-latest.tar.gpg"

printf '%s\n' "Wrote encrypted bundle: $OUTPUT"
printf '%s\n' "Latest copy: $NEXTCLOUD_DIR/opencode-secrets-latest.tar.gpg"
