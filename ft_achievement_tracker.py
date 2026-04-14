import random
from typing import Set, List


ACHIEVEMENTS: List[str] = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
]


def gen_player_achievements() -> Set[str]:
    count: int = random.randint(3, len(ACHIEVEMENTS))
    return set(random.sample(ACHIEVEMENTS, count))


def format_set(s: Set[str]) -> str:
    if len(s) == 0:
        return "set()"
    return "{" + ", ".join(f"’{item}’" for item in sorted(s)) + "}"


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice: Set[str] = gen_player_achievements()
    bob: Set[str] = gen_player_achievements()
    charlie: Set[str] = gen_player_achievements()
    dylan: Set[str] = gen_player_achievements()

    print(f"Player Alice: {format_set(alice)}")
    print(f"Player Bob: {format_set(bob)}")
    print(f"Player Charlie: {format_set(charlie)}")
    print(f"Player Dylan: {format_set(dylan)}")

    all_distinct: Set[str] = set.union(alice, bob, charlie, dylan)

    common: Set[str] = set.intersection(alice, bob, charlie, dylan)

    print(f"All distinct achievements: {format_set(all_distinct)}")
    print(f"Common achievements: {format_set(common)}")

    only_alice: Set[str] = set.difference(alice, bob, charlie, dylan)
    only_bob: Set[str] = set.difference(bob, alice, charlie, dylan)
    only_charlie: Set[str] = set.difference(charlie, alice, bob, dylan)
    only_dylan: Set[str] = set.difference(dylan, alice, bob, charlie)

    print(f"Only Alice has: {format_set(only_alice)}")
    print(f"Only Bob has: {format_set(only_bob)}")
    print(f"Only Charlie has: {format_set(only_charlie)}")
    print(f"Only Dylan has: {format_set(only_dylan)}")

    missing_alice: Set[str] = set.difference(all_distinct, alice)
    missing_bob: Set[str] = set.difference(all_distinct, bob)
    missing_charlie: Set[str] = set.difference(all_distinct, charlie)
    missing_dylan: Set[str] = set.difference(all_distinct, dylan)

    print(f"Alice is missing: {format_set(missing_alice)}")
    print(f"Bob is missing: {format_set(missing_bob)}")
    print(f"Charlie is missing: {format_set(missing_charlie)}")
    print(f"Dylan is missing: {format_set(missing_dylan)}")


if __name__ == "__main__":
    main()
