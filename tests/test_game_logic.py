from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_score_update_wrong_guess():
    # Score should decrease by 5 for wrong guesses
    initial_score = 50
    new_score_high = update_score(initial_score, "Too High", 1)
    assert new_score_high == 45
    new_score_low = update_score(initial_score, "Too Low", 2)
    assert new_score_low == 45
