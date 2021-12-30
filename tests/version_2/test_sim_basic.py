import pytest
from tests.flo import diff
from game_of_greed.game_logic import Game

pytestmark = [pytest.mark.version_2]

# @pytest.mark.skip('Pending')
def test_quitter():
    game = Game()
    # diffs = diff(game.play, path="../game-of-greed/tests/version_2/quitter.sim.txt")
    diffs = diff(game.play, path="version_2/quitter.sim.txt")
    assert not diffs, diffs

# @pytest.mark.skip('Pending')
def test_one_and_done():
    game = Game()
    diffs = diff(game.play, path="version_2/one_and_done.sim.txt")
    assert not diffs, diffs

# @pytest.mark.skip('Pending')
def test_single_bank():
    game = Game()
    diffs = diff(
        game.play, path="version_2/bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs

# @pytest.mark.skip('Pending')
def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(
        game.play, path="version_2/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs
