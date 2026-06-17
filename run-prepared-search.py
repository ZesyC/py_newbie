from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).parent
AI_DIR = ROOT / "AI"


def load_module(path):
    module_name = path.stem.replace("-", "_")
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def print_title(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_8_puzzle():
    prepare = load_module(AI_DIR / "prepare-8-puzzle.py")

    bfs_file = load_module(AI_DIR / "bfs.py")
    dfs_file = load_module(AI_DIR / "dfs.py")
    ids_file = load_module(AI_DIR / "IDS.py")
    ucs_file = load_module(AI_DIR / "UCS.py")
    astar_file = load_module(AI_DIR / "A-Star.py")
    ida_file = load_module(AI_DIR / "IDA-Star.py")
    greedy_file = load_module(AI_DIR / "Greedy_Best-first.py")
    hill_file = load_module(AI_DIR / "Hill-Climbing.py")
    beam_file = load_module(AI_DIR / "Beam-Search.py")
    puzzle_bfs_file = load_module(AI_DIR / "8-puzzle.py")
    puzzle_astar_file = load_module(AI_DIR / "8-puzzle-2.py")

    start = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    graph, weighted_graph, heuristic, start, goals = prepare.build_graph(start)

    print_title("8-PUZZLE - BFS")
    bfs_file.BreadthFirstSearch(graph, start, goals).bfs(verbose=True)

    print_title("8-PUZZLE - DFS")
    dfs_file.DFSGraphSearch(graph, start, goals).dfs(verbose=True)

    print_title("8-PUZZLE - IDS")
    ids_file.IterativeDeepeningSearch(graph, start, goals).ids(
        max_depth=3,
        verbose=True,
    )

    print_title("8-PUZZLE - UCS")
    ucs_file.UniformCostSearch(weighted_graph, start, goals).ucs(verbose=True)

    print_title("8-PUZZLE - A*")
    astar_file.AStarSearch(weighted_graph, heuristic, start, goals).a_star(
        verbose=True,
    )

    print_title("8-PUZZLE - IDA*")
    ida_file.IDAStarSearch(weighted_graph, heuristic, start, goals).ida_star(
        verbose=True,
    )

    print_title("8-PUZZLE - GREEDY BEST-FIRST")
    greedy_file.GreedyBestFirstSearch(graph, heuristic, start, goals).greedy(
        verbose=True,
    )

    print_title("8-PUZZLE - HILL CLIMBING")
    hill_file.HillClimbingSearch(graph, heuristic, start, goals).hill_climbing(
        verbose=True,
    )

    print_title("8-PUZZLE - BEAM SEARCH")
    beam_file.BeamSearch(graph, heuristic, start, goals, width=2).beam_search(
        verbose=True,
    )

    print_title("8-PUZZLE - CLASS RIENG TRONG AI/8-puzzle.py")
    puzzle_bfs_file.EightPuzzle(start).bfs(verbose=True)

    print_title("8-PUZZLE - CLASS RIENG TRONG AI/8-puzzle-2.py")
    puzzle_astar_file.EightPuzzle(start).a_star(verbose=True)


def run_missionaries_cannibals():
    prepare = load_module(AI_DIR / "prepare-missionaries-cannibals.py")

    bfs_file = load_module(AI_DIR / "bfs.py")
    dfs_file = load_module(AI_DIR / "dfs.py")
    ids_file = load_module(AI_DIR / "IDS.py")
    ucs_file = load_module(AI_DIR / "UCS.py")
    astar_file = load_module(AI_DIR / "A-Star.py")
    ida_file = load_module(AI_DIR / "IDA-Star.py")
    greedy_file = load_module(AI_DIR / "Greedy_Best-first.py")
    hill_file = load_module(AI_DIR / "Hill-Climbing.py")
    beam_file = load_module(AI_DIR / "Beam-Search.py")
    mc_file = load_module(AI_DIR / "MissionariesCannibals.py")

    graph, weighted_graph, heuristic, start, goals = prepare.build_graph()

    print_title("MISSIONARIES CANNIBALS - BFS")
    bfs_file.BreadthFirstSearch(graph, start, goals).bfs(verbose=True)

    print_title("MISSIONARIES CANNIBALS - DFS")
    dfs_file.DFSGraphSearch(graph, start, goals).dfs(verbose=True)

    print_title("MISSIONARIES CANNIBALS - IDS")
    ids_file.IterativeDeepeningSearch(graph, start, goals).ids(
        max_depth=20,
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - UCS")
    ucs_file.UniformCostSearch(weighted_graph, start, goals).ucs(verbose=True)

    print_title("MISSIONARIES CANNIBALS - A*")
    astar_file.AStarSearch(weighted_graph, heuristic, start, goals).a_star(
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - IDA*")
    ida_file.IDAStarSearch(weighted_graph, heuristic, start, goals).ida_star(
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - GREEDY BEST-FIRST")
    greedy_file.GreedyBestFirstSearch(graph, heuristic, start, goals).greedy(
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - HILL CLIMBING")
    hill_file.HillClimbingSearch(graph, heuristic, start, goals).hill_climbing(
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - BEAM SEARCH")
    beam_file.BeamSearch(graph, heuristic, start, goals, width=2).beam_search(
        verbose=True,
    )

    print_title("MISSIONARIES CANNIBALS - CLASS RIENG TRONG AI")
    mc_file.MissionariesCannibals().bfs(verbose=True)


if __name__ == "__main__":
    run_8_puzzle()
    run_missionaries_cannibals()
