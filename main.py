from argparse import ArgumentParser


def run():
    parser = ArgumentParser(description="Grader CLI")

    parser.add_argument("task_name", help="name of the task to grade")
    parser.add_argument("solution_path", help="path to the solution file")

    args = parser.parse_args()

    print(args.task_name)


if __name__ == "__main__":
    run()
