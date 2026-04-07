"""Smoke test for importing the locally built grain package."""

from __future__ import annotations

import grain


def main() -> None:
  print("grain import ok")
  print(f"version={getattr(grain, '__version__', 'unknown')}")


if __name__ == "__main__":
  main()
