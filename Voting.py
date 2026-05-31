# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class Voting(gl.Contract):
    candidates: str       
    votes: str            
    has_voted: str        

    def __init__(self, candidate_names: str):
        self.candidates = candidate_names
        names = candidate_names.split(",") if candidate_names else []
        self.votes = ",".join(["0"] * len(names))
        self.has_voted = ""

    @gl.public.write
    def vote(self, candidate_index: int, voter_id: str) -> None:
        
        voted = self.has_voted.split(",") if self.has_voted else []
        assert voter_id not in voted, "This voter has already voted"

    
        candidates = self.candidates.split(",")
        assert 0 <= candidate_index < len(candidates), "Invalid candidate"

        votes_list = [int(v) for v in self.votes.split(",")]
        votes_list[candidate_index] += 1
        self.votes = ",".join(str(v) for v in votes_list)

        
        voted.append(voter_id)
        self.has_voted = ",".join(voted)

    @gl.public.view
    def get_candidates(self) -> str:
        names = self.candidates.split(",")
        votes_list = [int(v) for v in self.votes.split(",")]
        return ",".join(f"{names[i]}:{votes_list[i]}" for i in range(len(names)))