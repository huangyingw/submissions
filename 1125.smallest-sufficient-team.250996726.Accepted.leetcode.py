class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        skill_to_int = {skill: i for i, skill in enumerate(req_skills)}
        people_skills = [0] * len(people)
        for i, person in enumerate(people):
            for skill in person:
                people_skills[i] |= 1 << skill_to_int[skill]
        self.has_skills = 0
        self.smallest_team = list(range(len(req_skills) + 1))
        team = []
        def helper(next_skill):
            if len(team) >= len(self.smallest_team):
                return
            if next_skill == len(req_skills):
                self.smallest_team = team[:]
                return
            if self.has_skills & (1 << next_skill):
                helper(next_skill + 1)
            else:
                for i, person_skills in enumerate(people_skills):
                    if person_skills & (1 << next_skill):
                        copy_skills = self.has_skills
                        self.has_skills |= person_skills
                        team.append(i)
                        helper(next_skill + 1)
                        team.pop()
                        self.has_skills = copy_skills
        helper(0)
        return self.smallest_team
