from interactive_bash.main import InteractiveSession

HELP = 'Доступные команды:\n\n\
  help         - вывести справку по командам\n\
  add-review   - добавить отзыв\n\
  list-reviews - показать все отзывы\n\
  clear        - удалить все отзывы\n'

async def help_test():
    solution = InteractiveSession(path = "solution.sh" )
    try:
        await solution.enterLine("help")
        await solution.expectOutput(HELP)
    finally:
        await solution.terminate()

async def add_review_test():
    solution = InteractiveSession(path = "solution.sh" )
    try:
        await solution.enterLine("add-review")
        await solution.enterLine("review 0")
        await solution.expectOutput("Спасибо за ваш отзыв!")
    finally:
        await solution.terminate()

async def kist_reviews_test():
    solution = InteractiveSession(path = "solution.sh" )
    # Отзывов ещё нет
    try:
        await solution.enterLine("list-reviews")
        await solution.expectOutput("Отзывов ещё нет :(")
    finally:
        await solution.terminate()

    solution = InteractiveSession(path = "solution.sh" )
    # Отображает сохранённый отзыв
    try:
        await solution.enterLine("add-review")
        await solution.enterLine("review 0")
        await solution.skipLines(1)

        await solution.enterLine("list-reviews")
        await solution.expectOutput("-----\nreview 0\n-----")
    finally:
        await solution.terminate()

    solution = InteractiveSession(path = "solution.sh" )
    # Отображает новые отзывы в конце списка
    try:
        await solution.enterLine("add-review")
        await solution.enterLine("review 0")
        await solution.skipLines(1)

        await solution.enterLine("add-review")
        await solution.enterLine("review 1")
        await solution.skipLines(1)

        await solution.enterLine("list-reviews")
        await solution.expectOutput("-----\nreview 0\n-----\nreview 1\n-----")
    finally:
        await solution.terminate()

async def clear_test():
    solution = InteractiveSession(path = "solution.sh" )
    try:
        await solution.enterLine("add-review")
        await solution.enterLine("review 0")
        await solution.skipLines(1)

        await solution.enterLine("clear")
        await solution.expectOutput("Все отзывы удалены")

        await solution.enterLine("list-reviews")
        await solution.expectOutput("Отзывов ещё нет :(")
    finally:
        await solution.terminate()

async def unknown_test():
    solution = InteractiveSession(path = "solution.sh" )
    try:
        await solution.enterLine("blah-blah")
        await solution.expectOutput(
        "Неизвестная команда. Введите help, чтобы узнать о доступных командах"
    )
    finally:
        await solution.terminate()