#!/bin/bash
# ELEANOR: The Bloodline Curse — Ren'Py launcher helper
# Usage:
#   ./run.sh            → run the game (GUI)
#   ./run.sh lint       → run Ren'Py lint
#   ./run.sh compile    → bytecode compile check
#   ./run.sh test       → run the game and quit after 1s (smoke test)

RENPY="${RENPY:-/Users/shieldjaguar/workspace/renpy-sdk/renpy-8.6.0-sdk/renpy.sh}"
GAME_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -x "$RENPY" ]; then
  echo "❌ Ren'Py SDK not found at: $RENPY"
  echo "   Set the RENPY env var to your renpy.sh path."
  exit 1
fi

case "${1:-run}" in
  run)   "$RENPY" "$GAME_DIR" ;;
  lint)  "$RENPY" "$GAME_DIR" lint ;;
  compile) "$RENPY" "$GAME_DIR" compile ;;
  test)
    # Launch then quit after ~2s to smoke-test startup
    "$RENPY" "$GAME_DIR" test 2>&1 | tail -20
    echo "Exit code: $?"
    ;;
  *) echo "Usage: ./run.sh [run|lint|compile|test]"; exit 1 ;;
esac
