"""Generate the deterministic Week 02 temperature datasets."""

from pathlib import Path


ROOM_COUNT = 1_000
HOUR_COUNT = 24
MISSING_COUNT = 7
HOURLY_PATTERN = (
    -22, -24, -25, -26, -25, -22, -17, -10,
    -3, 4, 10, 15, 19, 22, 23, 22,
    18, 13, 8, 3, -3, -9, -14, -18,
)


def build_readings() -> list[int]:
    """Return temperatures in tenths of a degree, ordered by room then hour."""
    return [
        210 + (room_id % 19) + HOURLY_PATTERN[hour] + ((room_id * 7 + hour * 3) % 5 - 2)
        for room_id in range(ROOM_COUNT)
        for hour in range(HOUR_COUNT)
    ]


def write_csv(path: Path, readings: list[int]) -> None:
    rows = ["temperature_tenths_c", *(str(value) for value in readings)]
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    complete = build_readings()
    write_csv(data_dir / "temperature_complete.csv", complete)
    write_csv(data_dir / "temperature_missing.csv", complete[:-MISSING_COUNT])


if __name__ == "__main__":
    main()
