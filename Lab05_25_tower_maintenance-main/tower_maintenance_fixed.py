"""Track maintenance history and risk for telecom towers."""

import sqlite3


class TowerMaintenance:
    """Store tower maintenance records and provide maintenance queries."""

    def __init__(self):
        """Initialize an in-memory database and the service counter."""
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            """
            CREATE TABLE towers (
                id INTEGER PRIMARY KEY,
                site TEXT,
                last_service INTEGER,
                faults INTEGER
            )
            """
        )
        self.service_count = 0

    def add_tower(self, site, last_service, faults=0):
        """Add a tower with its last service year and current fault count."""
        self.connection.execute(
            """
            INSERT INTO towers (site, last_service, faults)
            VALUES (?, ?, ?)
            """,
            (site, last_service, faults),
        )
        self.connection.commit()

    def service_tower(self, tower_id, year):
        """Record a tower service and clear its fault count."""
        cursor = self.connection.execute(
            """
            UPDATE towers
            SET last_service = ?, faults = 0
            WHERE id = ?
            """,
            (year, tower_id),
        )
        if cursor.rowcount == 0:
            raise ValueError(f"No tower found with ID {tower_id}.")

        self.connection.commit()
        self.service_count += 1

    def overdue_towers(self, year):
        """Return sites not serviced within the last two years."""
        rows = self.connection.execute(
            "SELECT site, last_service FROM towers"
        ).fetchall()
        return [
            site
            for site, last_service in rows
            if year - last_service >= 2
        ]

    def risk_level(self, tower_id):
        """Return the risk level for a tower based on its fault count."""
        row = self.connection.execute(
            "SELECT faults FROM towers WHERE id = ?",
            (tower_id,),
        ).fetchone()
        if row is None:
            raise ValueError(f"No tower found with ID {tower_id}.")

        if row[0] > 3:
            return "high"
        return "normal"

    def snapshot(self):
        """Return all tower records as database rows."""
        return self.connection.execute(
            "SELECT * FROM towers"
        ).fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()


def main():
    """Run a short demonstration of the maintenance tracker."""
    tracker = TowerMaintenance()
    try:
        tracker.add_tower("Ridge-A", 2021, 5)
        tracker.add_tower("Coast-B", 2024)
        tracker.service_tower(2, 2025)
        total = len(tracker.snapshot())
        print(
            tracker.overdue_towers(2025),
            tracker.risk_level(1),
            total,
            tracker.service_count,
        )
    finally:
        tracker.close()


if __name__ == "__main__":
    main()
