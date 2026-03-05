from src.stats.matchstats import MatchStats
from src.stats.winstats import WinStats


def test_match_stats():
    scores = [120, 150, 98, 201, 175]

    stats = MatchStats(scores)

    print("----- Match Stats -----")
    print("Scores:", scores)
    print("Total Runs:", stats.get_total_runs())
    print("Average Score:", stats.get_average_score())
    print("Highest Score:", stats.get_highest_score())
    print("Lowest Score:", stats.get_lowest_score())
    print("Score Range:", stats.get_score_range())


def test_win_stats():
    results = ["W", "L", "W", "W", "L", "W"]

    stats = WinStats(results)

    print("\n----- Win Stats -----")
    print("Results:", results)
    print("Total Matches:", stats.get_total_matches())
    print("Total Wins:", stats.get_total_wins())
    print("Total Losses:", stats.get_total_losses())
    print("Win Rate:", stats.get_win_rate())


if __name__ == "__main__":
    test_match_stats()
    test_win_stats()