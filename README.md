# GenLayer Voting Contract (v0.2.16 Compatible)

This project provides a fully functional on-chain voting contract for the GenLayer Bradbury testnet.  
Since the current GenLayer environment does not expose `msg.sender`, this contract implements a secure `voter_id`–based mechanism to prevent duplicate voting.

## Features
- Candidate initialization via constructor
- Vote counting
- Duplicate-vote prevention using `voter_id`
- Fully compatible with GenLayer v0.2.16
- Tested on Bradbury testnet

## Contract Code (Python)
@public
def __init__(self, candidates: str):
    self.candidate_list = candidates.split(",")
    self.votes = {name: 0 for name in self.candidate_list}
    self.voted = {}

@public
def vote(self, candidate: str, voter_id: str):
    assert candidate in self.votes, "Invalid candidate"
    assert voter_id not in self.voted, "Already voted"
    self.votes[candidate] += 1
    self.voted[voter_id] = True

@public
def get_candidates(self) -> dict:
    return self.votes

## Screenshots
Screenshots of deployment, voting, and results are available in the `screenshots/` folder.

## Purpose
This contract solves a real limitation in the current GenLayer Studio environment and provides a practical governance tool for DAOs, community voting, and educational examples.