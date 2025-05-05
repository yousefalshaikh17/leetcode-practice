from typing import List
from os import listdir
from pathlib import Path

comment_prefix_by_extension = {
    "cpp": "//",
    "c": "//",
    "cs": "//",
    "php": "//",
    "swift": "//",
    "kt": "//",
    "ts": "//",
    "js": "//",
    "java": "//",
    "py": "#",
    "lua": "--",
    "luau": "--",
}

language_by_extension = {
    "cpp": "C++",
    "c": "C",
    "cs": "C#",
    "php": "PHP",
    "swift": "Swift",
    "kt": "Kotlin",
    "ts": "TypeScript",
    "js": "JavaScript",
    "java": "Java",
    "py": "Python",
    "lua": "Lua",
    "luau": "Luau",
}


solutions_path = Path('solutions')

class LeetCodeSolvedProblem:

    class Solution:
        def __init__(self, file_name: str):
            self.file_name = file_name
        
        def get_extension(self):
            return Path(self.file_name).suffix[1:]
        
        def get_language(self):
            return language_by_extension[self.get_extension()]
        
        def get_path(self):
            return solutions_path.joinpath(Path(self.file_name))

    def __init__(self, id: int, name: str, topics: List[str]):
        self.id = id
        self.name = name
        self.topics = [topic.strip() for topic in topics]

        prefix_str = f"{id}-"
        self.solutions = [LeetCodeSolvedProblem.Solution(file_name) for file_name in listdir(solutions_path) if file_name.startswith(prefix_str)]

    @classmethod
    def from_solution_file(self, file_name: str):
        # Filter out directory navigation
        file_name = Path(file_name).name

        problem_id = int(file_name[:file_name.find('-')])

        if file_name not in listdir(solutions_path):
            raise FileNotFoundError(f"File {file_name} does not exist in the solutions folder.")
        
        file_path = solutions_path.joinpath(Path(file_name))
        extension = file_path.suffix[1:]

        comment_prefix = comment_prefix_by_extension.get(extension, "//")

        def get_comment_text(line: str):
            return line[len(comment_prefix):].strip()

        with open(file_path, 'r') as file:
            # Problem name line
            first_line = file.readline().strip()

            if not first_line.startswith(comment_prefix):
                raise ValueError("First line does not contain a valid comment prefix.")
            
            text_after_comment = get_comment_text(first_line)
            problem_name = text_after_comment.split('. ')[-1]

            # Topic list line
            second_line = file.readline().strip()
            if not second_line.startswith(comment_prefix):
                raise ValueError("Second line does not contain a valid comment prefix.")
            
            topic_str = get_comment_text(second_line)
            topic_str = topic_str[len('Topics:'):].strip()
            
            topics = [topic.strip() for topic in topic_str.split(', ')]
        
        return LeetCodeSolvedProblem(problem_id, problem_name, topics)
    
    @staticmethod
    def get_all_solved_problems():
        problems = []
        seen_ids = set()
        for file_name in listdir(solutions_path):
            id = file_name[:file_name.find('-')]
            if id in seen_ids:
                continue

            seen_ids.add(id)
            problems.append(LeetCodeSolvedProblem.from_solution_file(file_name))

        return problems
    
    def __str__(self):
        topics_str = ", ".join(self.topics)
        return f"[{self.id}] {self.name} — Topics: {topics_str} — Files: {len(self.solutions)} solution(s)"
    
    def __lt__(self, other):
        if not isinstance(other, LeetCodeSolvedProblem):
            return NotImplemented
        return self.id < other.id


solved_problems = LeetCodeSolvedProblem.get_all_solved_problems()

# Sort them to make it easier to organize
solved_problems.sort()

topics_map = {}

for problem in solved_problems:
    for topic in problem.topics:
        if topic not in topics_map:
            topics_map[topic] = []
        
        topics_map[topic].append(problem)

# Sort topic maps based on most solved (And then alphabetically)
sorted_topics_map = sorted(
    topics_map.items(),
    key=lambda item: (-len(item[1]), item[0])
)

def update_topics_page(topics_map):
    topics_path = 'topics.md'
    with open(topics_path, 'r') as file:
        lines = file.readlines()

    # Find first use of Heading 2
    for i, line in enumerate(lines):
        if line.strip().startswith('## '):
            topics_header = ''.join(lines[0:i])
            break

    with open(topics_path, 'w') as file:
        # Add header
        file.write(topics_header)

        for topic, problems in sorted_topics_map:
            # Write header
            file.write(f"## {topic}\n\n")
            # Write each entry
            file.writelines([
                f"**{problem.id}.** {problem.name}: { ' | '.join([f'[{solution.get_language()}]({str(solution.get_path())})' for solution in problem.solutions]) }  \n" for problem in problems
            ])
            file.write("\n")

# @TODO: This function isn't optimal. Update it at a later time.
def update_readme_topics(topic_names):
    readme_path = 'README.md'
    
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    start_idx = None
    end_idx = None

    # Find start of the ## Topics section
    for i, line in enumerate(lines):
        if line.strip().lower() == '## topics':
            start_idx = i
            break

    if start_idx is None:
        raise ValueError("The README does not contain a '## Topics' section.")

    # Find where the Topics section ends
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith('## '):
            end_idx = j
            break
    else:
        end_idx = len(lines)

    # Format new topic list
    new_section = [lines[start_idx], '\n']  # Keep the "## Topics" header
    for topic in topic_names:
        slug = topic.lower().replace(' ', '-')
        new_section.append(f"- [{topic}](topics.md#{slug})\n")
    new_section += '\n'

    # Merge changes
    updated_lines = lines[:start_idx] + new_section + lines[end_idx:]

    with open(readme_path, 'w') as file:
        file.writelines(updated_lines)


update_readme_topics([topic for topic, _ in sorted_topics_map])
update_topics_page(sorted_topics_map)